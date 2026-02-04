"""
Job Description Matcher with semantic analysis and intelligent recommendations.
"""

import re
from typing import Dict, List, Set, Tuple
from collections import Counter

class JDMatcher:
    def __init__(self):
        self.stop_words = {
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
            "of", "with", "by", "from", "as", "is", "was", "are", "were", "be",
            "been", "being", "have", "has", "had", "do", "does", "did", "will",
            "would", "should", "could", "may", "might", "must", "can", "this",
            "that", "these", "those", "i", "you", "he", "she", "it", "we", "they",
            "who", "what", "where", "when", "why", "how", "all", "each", "every",
            "both", "few", "more", "most", "other", "some", "such", "than", "too",
            "very", "our", "your", "their"
        }
    
    def analyze_jd_match(
        self,
        resume_text: str,
        jd_text: str,
        extracted_skills: List[str]
    ) -> Dict:
        """
        Comprehensive JD matching analysis.
        """
        
        if not jd_text or len(jd_text.strip()) < 30:
            return {
                "match_score": None,
                "analysis": "No job description provided",
                "recommendations": []
            }
        
        # Extract keywords from both texts
        resume_keywords = self._extract_keywords(resume_text)
        jd_keywords = self._extract_keywords(jd_text)
        
        # Extract skills from JD
        jd_required_skills = self._extract_jd_skills(jd_text)
        
        # Calculate matches
        keyword_matches = resume_keywords.intersection(jd_keywords)
        keyword_missing = jd_keywords - resume_keywords
        
        skill_matches = set(extracted_skills).intersection(jd_required_skills)
        skill_missing = jd_required_skills - set(extracted_skills)
        
        # Calculate scores
        keyword_score = self._calculate_match_score(keyword_matches, jd_keywords)
        skill_score = self._calculate_match_score(skill_matches, jd_required_skills)
        
        # Overall match score (weighted average)
        overall_score = (keyword_score * 0.6 + skill_score * 0.4)
        
        # Analyze sections
        section_alignment = self._analyze_section_alignment(resume_text, jd_text)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            overall_score,
            skill_missing,
            keyword_missing,
            section_alignment
        )
        
        # Identify must-have vs nice-to-have
        must_have, nice_to_have = self._categorize_requirements(jd_text, skill_missing)
        
        return {
            "match_score": round(overall_score, 2),
            "grade": self._get_match_grade(overall_score),
            "breakdown": {
                "keyword_match": round(keyword_score, 2),
                "skill_match": round(skill_score, 2)
            },
            "matched": {
                "skills": sorted(list(skill_matches)),
                "keywords": sorted(list(keyword_matches))[:20]
            },
            "missing": {
                "must_have_skills": sorted(list(must_have))[:10],
                "nice_to_have_skills": sorted(list(nice_to_have))[:10],
                "keywords": sorted(list(keyword_missing))[:15]
            },
            "section_alignment": section_alignment,
            "recommendations": recommendations,
            "coverage": {
                "skills": f"{len(skill_matches)}/{len(jd_required_skills)}",
                "keywords": f"{len(keyword_matches)}/{len(jd_keywords)}"
            }
        }
    
    def _extract_keywords(self, text: str) -> Set[str]:
        """Extract meaningful keywords from text."""
        # Remove special characters and numbers
        text_clean = re.sub(r'[^a-zA-Z\s]', ' ', text.lower())
        
        # Extract words
        words = text_clean.split()
        
        # Filter stop words and short words
        keywords = {
            word for word in words
            if len(word) > 3 and word not in self.stop_words
        }
        
        return keywords
    
    def _extract_jd_skills(self, jd_text: str) -> Set[str]:
        """Extract required skills from job description."""
        skills = set()
        jd_lower = jd_text.lower()
        
        # Common skill patterns
        skill_patterns = [
            r'required skills?:?\s*([^\n]+)',
            r'qualifications?:?\s*([^\n]+)',
            r'experience (?:with|in):?\s*([^\n]+)',
            r'proficient (?:with|in):?\s*([^\n]+)',
            r'knowledge of:?\s*([^\n]+)',
        ]
        
        for pattern in skill_patterns:
            matches = re.finditer(pattern, jd_lower)
            for match in matches:
                skill_text = match.group(1)
                # Split by common separators
                extracted = re.split(r'[,;•\n]', skill_text)
                for skill in extracted:
                    skill = skill.strip()
                    if len(skill) > 2 and len(skill) < 50:
                        skills.add(skill)
        
        # Common technology keywords
        tech_keywords = [
            "python", "java", "javascript", "sql", "aws", "azure", "gcp",
            "docker", "kubernetes", "react", "angular", "node", "git",
            "machine learning", "data science", "analytics", "tableau",
            "power bi", "excel", "agile", "scrum", "jira"
        ]
        
        for keyword in tech_keywords:
            if keyword in jd_lower:
                skills.add(keyword)
        
        return skills
    
    def _calculate_match_score(self, matched: Set, total: Set) -> float:
        """Calculate match percentage."""
        if not total:
            return 100.0
        
        return (len(matched) / len(total)) * 100
    
    def _analyze_section_alignment(self, resume_text: str, jd_text: str) -> Dict:
        """Analyze how well resume sections align with JD requirements."""
        alignment = {}
        
        jd_lower = jd_text.lower()
        resume_lower = resume_text.lower()
        
        # Check for common requirements
        requirements = {
            "experience": ["years of experience", "experience in", "experience with"],
            "education": ["degree in", "bachelor", "master", "phd"],
            "certifications": ["certified", "certification", "license"],
            "leadership": ["lead", "manage", "supervise", "mentor"],
            "projects": ["project", "portfolio", "built", "developed"]
        }
        
        for req_type, keywords in requirements.items():
            jd_has = any(kw in jd_lower for kw in keywords)
            resume_has = any(kw in resume_lower for kw in keywords)
            
            if jd_has:
                alignment[req_type] = {
                    "required": True,
                    "present_in_resume": resume_has,
                    "status": "✅ Aligned" if resume_has else "❌ Missing"
                }
        
        return alignment
    
    def _categorize_requirements(
        self, jd_text: str, missing_skills: Set[str]
    ) -> Tuple[Set[str], Set[str]]:
        """Categorize missing skills into must-have and nice-to-have."""
        jd_lower = jd_text.lower()
        
        must_have = set()
        nice_to_have = set()
        
        # Must-have indicators
        must_have_patterns = [
            "required", "must have", "must be", "essential",
            "mandatory", "critical", "minimum"
        ]
        
        # Nice-to-have indicators
        nice_patterns = [
            "preferred", "nice to have", "bonus", "plus",
            "desired", "advantageous", "beneficial"
        ]
        
        for skill in missing_skills:
            # Check context around the skill
            pattern = r'.{0,100}' + re.escape(skill) + r'.{0,100}'
            matches = re.finditer(pattern, jd_lower)
            
            is_must_have = False
            is_nice = False
            
            for match in matches:
                context = match.group(0)
                
                if any(indicator in context for indicator in must_have_patterns):
                    is_must_have = True
                    break
                elif any(indicator in context for indicator in nice_patterns):
                    is_nice = True
            
            if is_must_have:
                must_have.add(skill)
            elif is_nice:
                nice_to_have.add(skill)
            else:
                # Default: put in nice-to-have
                nice_to_have.add(skill)
        
        return must_have, nice_to_have
    
    def _generate_recommendations(
        self,
        overall_score: float,
        skill_missing: Set[str],
        keyword_missing: Set[str],
        section_alignment: Dict
    ) -> List[str]:
        """Generate tailored recommendations."""
        recommendations = []
        
        # Overall assessment
        if overall_score >= 80:
            recommendations.append("🎯 Excellent match! Your resume aligns well with this JD.")
        elif overall_score >= 60:
            recommendations.append("✅ Good match! Address key gaps to strengthen your application.")
        elif overall_score >= 40:
            recommendations.append("⚠️ Moderate match. Significant improvements needed.")
        else:
            recommendations.append("❌ Low match. Consider if this role aligns with your background.")
        
        # Skill gaps
        if skill_missing:
            top_missing = list(skill_missing)[:5]
            recommendations.append(
                f"📚 Develop these skills: {', '.join(top_missing)}"
            )
        
        # Section alignment
        for req_type, data in section_alignment.items():
            if data["required"] and not data["present_in_resume"]:
                recommendations.append(
                    f"📝 Add {req_type} section highlighting relevant background."
                )
        
        # Keyword optimization
        if keyword_missing:
            recommendations.append(
                "🔑 Incorporate more JD keywords naturally throughout your resume."
            )
        
        # Tailor suggestion
        recommendations.append(
            "✏️ Tailor your resume: Mirror language from JD in your experience descriptions."
        )
        
        return recommendations[:8]
    
    def _get_match_grade(self, score: float) -> str:
        """Get match grade."""
        if score >= 90:
            return "A+ (Excellent Match)"
        elif score >= 80:
            return "A (Great Match)"
        elif score >= 70:
            return "B (Good Match)"
        elif score >= 60:
            return "C (Fair Match)"
        elif score >= 50:
            return "D (Weak Match)"
        else:
            return "F (Poor Match)"
    
    def generate_tailored_resume_tips(
        self, jd_text: str, resume_text: str
    ) -> List[str]:
        """Generate specific tips for tailoring resume to JD."""
        tips = []
        
        jd_lower = jd_text.lower()
        
        # Check for company culture keywords
        culture_keywords = {
            "innovative": "Highlight creative problem-solving and innovative projects",
            "collaborative": "Emphasize teamwork and cross-functional collaboration",
            "fast-paced": "Showcase ability to multitask and deliver under pressure",
            "data-driven": "Feature analytical projects with measurable outcomes",
            "customer-focused": "Demonstrate customer success stories and impact"
        }
        
        for keyword, tip in culture_keywords.items():
            if keyword in jd_lower:
                tips.append(f"💡 Company values '{keyword}': {tip}")
        
        # Check for seniority level
        if any(term in jd_lower for term in ["senior", "lead", "principal"]):
            tips.append("👔 Senior role: Emphasize leadership, mentoring, and strategic impact")
        elif any(term in jd_lower for term in ["junior", "entry", "associate"]):
            tips.append("🌱 Entry role: Focus on learning ability, projects, and foundational skills")
        
        return tips[:5]

jd_matcher = JDMatcher()