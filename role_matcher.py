"""
Intelligent role matcher using multiple scoring algorithms:
- Skill matching with weighted importance
- Context-aware matching
- Experience level consideration
- Industry-specific scoring
"""

from typing import List, Dict, Tuple
from data.job_database import JOB_DATABASE, SKILL_SYNONYMS

class RoleMatcher:
    def __init__(self):
        self.roles = JOB_DATABASE
        
    def match_roles(
        self,
        extracted_skills: List[str],
        skill_details: Dict,
        experience_years: int = 0,
        certifications: List[str] = None,
        education: List[Dict] = None
    ) -> List[Dict]:
        """
        Match resume to job roles using comprehensive scoring.
        
        Returns list of roles with detailed match information.
        """
        results = []
        
        for role_name, role_data in self.roles.items():
            match_result = self._calculate_match(
                role_name,
                role_data,
                extracted_skills,
                skill_details,
                experience_years,
                certifications or [],
                education or []
            )
            results.append(match_result)
        
        # Sort by overall score
        results.sort(key=lambda x: x["overall_score"], reverse=True)
        
        return results
    
    def _calculate_match(
        self,
        role_name: str,
        role_data: Dict,
        extracted_skills: List[str],
        skill_details: Dict,
        experience_years: int,
        certifications: List[str],
        education: List[Dict]
    ) -> Dict:
        """Calculate comprehensive match score for a role."""
        
        # Collect all required skills for the role
        required_skills = set([s.lower() for s in role_data.get("skills", [])])
        required_tools = set([s.lower() for s in role_data.get("tools", [])])
        required_soft_skills = set([s.lower() for s in role_data.get("soft_skills", [])])
        preferred_certs = set([c.lower() for c in role_data.get("certifications", [])])
        
        # Normalize extracted skills
        extracted_set = set([s.lower() for s in extracted_skills])
        
        # Calculate skill match
        skills_matched = self._match_with_synonyms(required_skills, extracted_set)
        tools_matched = self._match_with_synonyms(required_tools, extracted_set)
        soft_skills_matched = self._match_with_synonyms(required_soft_skills, extracted_set)
        
        # Calculate scores
        skill_score = self._calculate_coverage_score(skills_matched, required_skills) * 100
        tool_score = self._calculate_coverage_score(tools_matched, required_tools) * 100
        soft_skill_score = self._calculate_coverage_score(soft_skills_matched, required_soft_skills) * 100
        
        # Certification match
        cert_score = self._match_certifications(certifications, preferred_certs)
        
        # Experience relevance (basic estimation)
        experience_score = min(experience_years * 10, 100)
        
        # Weighted overall score
        overall_score = (
            skill_score * 0.40 +           # 40% weight on technical skills
            tool_score * 0.25 +             # 25% weight on tools
            soft_skill_score * 0.15 +       # 15% weight on soft skills
            cert_score * 0.10 +             # 10% weight on certifications
            experience_score * 0.10         # 10% weight on experience
        )
        
        # Calculate confidence level
        confidence = self._calculate_confidence(
            skill_score, tool_score, len(skills_matched), len(tools_matched)
        )
        
        # Missing skills analysis
        all_required = required_skills.union(required_tools)
        all_matched = skills_matched.union(tools_matched)
        missing_skills = all_required - all_matched
        
        # Prioritize missing skills by importance
        critical_missing = self._identify_critical_skills(
            missing_skills, role_data.get("keywords", [])
        )
        
        return {
            "role": role_name,
            "category": role_data.get("category", "General"),
            "overall_score": round(overall_score, 2),
            "confidence": confidence,
            "breakdown": {
                "technical_skills": round(skill_score, 2),
                "tools": round(tool_score, 2),
                "soft_skills": round(soft_skill_score, 2),
                "certifications": round(cert_score, 2),
                "experience": round(experience_score, 2)
            },
            "matched_skills": {
                "technical": sorted(list(skills_matched)),
                "tools": sorted(list(tools_matched)),
                "soft_skills": sorted(list(soft_skills_matched))
            },
            "missing_skills": {
                "critical": sorted(list(critical_missing))[:5],
                "all": sorted(list(missing_skills))[:10]
            },
            "match_count": {
                "technical": f"{len(skills_matched)}/{len(required_skills)}",
                "tools": f"{len(tools_matched)}/{len(required_tools)}",
                "total": f"{len(all_matched)}/{len(all_required)}"
            }
        }
    
    def _match_with_synonyms(self, required: set, extracted: set) -> set:
        """Match skills considering synonyms."""
        matched = set()
        
        for req_skill in required:
            # Direct match
            if req_skill in extracted:
                matched.add(req_skill)
                continue
            
            # Check synonyms
            if req_skill in SKILL_SYNONYMS:
                synonyms = [s.lower() for s in SKILL_SYNONYMS[req_skill]]
                if any(syn in extracted for syn in synonyms):
                    matched.add(req_skill)
                    continue
            
            # Check if req_skill is a synonym of something in extracted
            for ext_skill in extracted:
                if ext_skill in SKILL_SYNONYMS:
                    synonyms = [s.lower() for s in SKILL_SYNONYMS[ext_skill]]
                    if req_skill in synonyms:
                        matched.add(req_skill)
                        break
        
        return matched
    
    def _calculate_coverage_score(self, matched: set, required: set) -> float:
        """Calculate coverage score with weighted importance."""
        if not required:
            return 1.0
        
        coverage = len(matched) / len(required)
        
        # Bonus for having more than required
        if len(matched) > len(required):
            bonus = min(0.1, (len(matched) - len(required)) * 0.02)
            coverage = min(1.0, coverage + bonus)
        
        return coverage
    
    def _match_certifications(self, user_certs: List[str], preferred_certs: set) -> float:
        """Calculate certification match score."""
        if not preferred_certs:
            return 50.0  # Neutral score if no certs required
        
        user_certs_lower = set([c.lower() for c in user_certs])
        matches = 0
        
        for pref_cert in preferred_certs:
            # Partial matching for certifications
            if any(pref_cert in user_cert for user_cert in user_certs_lower):
                matches += 1
        
        if matches == 0:
            return 0.0
        
        return min(100.0, (matches / len(preferred_certs)) * 100)
    
    def _calculate_confidence(
        self, skill_score: float, tool_score: float, 
        skills_count: int, tools_count: int
    ) -> str:
        """Calculate confidence level of the match."""
        avg_score = (skill_score + tool_score) / 2
        total_matches = skills_count + tools_count
        
        if avg_score >= 80 and total_matches >= 8:
            return "Very High"
        elif avg_score >= 60 and total_matches >= 5:
            return "High"
        elif avg_score >= 40 and total_matches >= 3:
            return "Medium"
        elif avg_score >= 20:
            return "Low"
        else:
            return "Very Low"
    
    def _identify_critical_skills(self, missing_skills: set, keywords: List[str]) -> set:
        """Identify critical missing skills based on role keywords."""
        critical = set()
        keywords_lower = [k.lower() for k in keywords]
        
        for skill in missing_skills:
            # Check if skill appears in role keywords
            if any(keyword in skill or skill in keyword for keyword in keywords_lower):
                critical.add(skill)
        
        return critical
    
    def get_top_matches(self, all_matches: List[Dict], top_n: int = 5) -> List[Dict]:
        """Get top N matches with additional insights."""
        top_matches = all_matches[:top_n]
        
        # Add insights
        for match in top_matches:
            match["insights"] = self._generate_insights(match)
        
        return top_matches
    
    def _generate_insights(self, match: Dict) -> List[str]:
        """Generate actionable insights for a role match."""
        insights = []
        
        overall = match["overall_score"]
        breakdown = match["breakdown"]
        
        # Overall assessment
        if overall >= 80:
            insights.append(f"🎯 Excellent match for {match['role']}!")
        elif overall >= 60:
            insights.append(f"✅ Good match for {match['role']}.")
        elif overall >= 40:
            insights.append(f"⚠️ Moderate match - significant skill development needed.")
        else:
            insights.append(f"❌ Low match - consider building foundational skills first.")
        
        # Specific feedback
        if breakdown["technical_skills"] < 50:
            insights.append("Focus on building core technical skills for this role.")
        
        if breakdown["tools"] < 50:
            insights.append("Gain hands-on experience with industry-standard tools.")
        
        if breakdown["certifications"] < 30:
            insights.append("Consider relevant certifications to boost credibility.")
        
        # Positive reinforcement
        if breakdown["technical_skills"] >= 70:
            insights.append("Strong technical foundation for this role!")
        
        if breakdown["tools"] >= 70:
            insights.append("Good familiarity with relevant tools and technologies!")
        
        return insights

role_matcher = RoleMatcher()