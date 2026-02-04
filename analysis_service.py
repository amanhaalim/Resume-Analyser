"""
Main Resume Analysis Service
Orchestrates all analysis components to provide comprehensive resume insights.
"""

from typing import Dict, Optional
from utils.skill_extractor import skill_extractor
from utils.role_matcher import role_matcher
from utils.ats_analyzer import ats_analyzer
from utils.jd_matcher import jd_matcher

class ResumeAnalysisService:
    def __init__(self):
        self.skill_extractor = skill_extractor
        self.role_matcher = role_matcher
        self.ats_analyzer = ats_analyzer
        self.jd_matcher = jd_matcher
    
    def analyze_resume(
        self,
        resume_text: str,
        job_description: Optional[str] = None,
        target_role: Optional[str] = None
    ) -> Dict:
        """
        Perform comprehensive resume analysis.
        
        Args:
            resume_text: Extracted text from resume
            job_description: Optional job description for matching
            target_role: Optional specific role to evaluate against
        
        Returns:
            Comprehensive analysis results
        """
        
        # 1. Extract Skills and Components
        skill_analysis = self.skill_extractor.extract_skills(resume_text)
        certifications = self.skill_extractor.extract_certifications(resume_text)
        experience = self.skill_extractor.extract_years_of_experience(resume_text)
        education = self.skill_extractor.extract_education(resume_text)
        action_verbs = self.skill_extractor.extract_action_verbs(resume_text)
        metrics = self.skill_extractor.extract_metrics(resume_text)
        
        # 2. Detect Sections
        sections = self.ats_analyzer.detect_sections(resume_text)
        
        # 3. ATS Analysis
        ats_results = self.ats_analyzer.analyze_ats_score(
            resume_text,
            skill_analysis["skill_list"],
            sections,
            action_verbs,
            metrics
        )
        
        # 4. Role Matching
        role_matches = self.role_matcher.match_roles(
            skill_analysis["skill_list"],
            skill_analysis["skills"],
            experience.get("max_years", 0),
            certifications,
            education
        )
        
        top_roles = self.role_matcher.get_top_matches(role_matches, top_n=10)
        
        # 5. Job Description Matching (if provided)
        jd_analysis = None
        if job_description:
            jd_analysis = self.jd_matcher.analyze_jd_match(
                resume_text,
                job_description,
                skill_analysis["skill_list"]
            )
            
            # Get tailored tips
            tailored_tips = self.jd_matcher.generate_tailored_resume_tips(
                job_description,
                resume_text
            )
            jd_analysis["tailored_tips"] = tailored_tips
        
        # 6. Generate Overall Recommendations
        overall_recommendations = self._generate_overall_recommendations(
            ats_results,
            top_roles,
            skill_analysis,
            jd_analysis
        )
        
        # 7. Calculate Resume Health Score
        health_score = self._calculate_health_score(
            ats_results["overall_score"],
            len(skill_analysis["skill_list"]),
            len(action_verbs),
            len(metrics),
            sections
        )
        
        return {
            "resume_health": {
                "overall_score": health_score,
                "status": self._get_health_status(health_score)
            },
            "ats_analysis": ats_results,
            "skills": {
                "extracted_skills": skill_analysis["skill_list"],
                "skill_details": skill_analysis["skills"],
                "total_skills": skill_analysis["total_unique_skills"],
                "high_confidence_skills": skill_analysis["high_confidence_skills"],
                "certifications": certifications
            },
            "experience": {
                **experience,
                "education": education
            },
            "role_matching": {
                "top_matches": top_roles[:5],
                "all_categories": self._group_matches_by_category(role_matches),
                "best_fit_role": top_roles[0] if top_roles else None
            },
            "content_analysis": {
                "action_verbs": action_verbs[:15],
                "quantifiable_metrics": metrics,
                "sections_detected": sections,
                "total_action_verbs": len(action_verbs),
                "total_metrics": len(metrics)
            },
            "job_description_match": jd_analysis,
            "recommendations": {
                "overall": overall_recommendations,
                "priority_actions": self._get_priority_actions(
                    ats_results,
                    skill_analysis,
                    jd_analysis
                )
            },
            "insights": self._generate_insights(
                ats_results,
                top_roles,
                skill_analysis,
                experience
            )
        }
    
    def _generate_overall_recommendations(
        self,
        ats_results: Dict,
        role_matches: list,
        skill_analysis: Dict,
        jd_analysis: Optional[Dict]
    ) -> list:
        """Generate overall recommendations combining all analyses."""
        recommendations = []
        
        # ATS recommendations
        if ats_results["overall_score"] < 70:
            recommendations.extend(ats_results["priority_improvements"][:2])
        
        # Role-specific recommendations
        if role_matches:
            best_role = role_matches[0]
            if best_role["overall_score"] < 70:
                recommendations.append(
                    f"🎯 To better match {best_role['role']}: "
                    f"Add {', '.join(best_role['missing_skills']['critical'][:3])}"
                )
        
        # Skill diversity
        if skill_analysis["total_unique_skills"] < 10:
            recommendations.append(
                "📚 Expand skill set: Add 5-8 more relevant technical skills"
            )
        
        # JD-specific recommendations
        if jd_analysis and jd_analysis["match_score"] and jd_analysis["match_score"] < 70:
            must_have = jd_analysis["missing"]["must_have_skills"]
            if must_have:
                recommendations.append(
                    f"⚠️ Critical JD requirements missing: {', '.join(must_have[:3])}"
                )
        
        return recommendations[:10]
    
    def _calculate_health_score(
        self,
        ats_score: float,
        skill_count: int,
        verb_count: int,
        metric_count: int,
        sections: Dict
    ) -> float:
        """Calculate overall resume health score."""
        
        # ATS Score (40%)
        ats_component = (ats_score / 100) * 40
        
        # Skills (25%)
        skill_score = min(skill_count / 15, 1.0) * 25
        
        # Content Quality (20%)
        verb_score = min(verb_count / 10, 1.0) * 10
        metric_score = min(metric_count / 5, 1.0) * 10
        content_component = verb_score + metric_score
        
        # Completeness (15%)
        required_sections = ["experience", "education", "skills"]
        section_count = sum(1 for s in required_sections if sections.get(s, False))
        completeness = (section_count / len(required_sections)) * 15
        
        total_score = ats_component + skill_score + content_component + completeness
        
        return round(total_score, 2)
    
    def _get_health_status(self, score: float) -> str:
        """Get resume health status."""
        if score >= 85:
            return "Excellent 🌟"
        elif score >= 70:
            return "Good ✅"
        elif score >= 55:
            return "Fair ⚠️"
        else:
            return "Needs Improvement 🔧"
    
    def _group_matches_by_category(self, role_matches: list) -> Dict:
        """Group role matches by industry category."""
        categories = {}
        
        for match in role_matches:
            category = match["category"]
            if category not in categories:
                categories[category] = []
            
            categories[category].append({
                "role": match["role"],
                "score": match["overall_score"],
                "confidence": match["confidence"]
            })
        
        # Sort each category by score
        for category in categories:
            categories[category].sort(key=lambda x: x["score"], reverse=True)
            categories[category] = categories[category][:3]  # Top 3 per category
        
        return categories
    
    def _get_priority_actions(
        self,
        ats_results: Dict,
        skill_analysis: Dict,
        jd_analysis: Optional[Dict]
    ) -> list:
        """Get top priority actions for immediate improvement."""
        actions = []
        
        # Check critical ATS issues
        if ats_results["overall_score"] < 60:
            actions.append({
                "priority": "CRITICAL",
                "action": "ATS Optimization",
                "description": "Your resume may not pass ATS screening",
                "steps": ats_results["priority_improvements"][:2]
            })
        
        # Check skill gaps
        if skill_analysis["total_unique_skills"] < 8:
            actions.append({
                "priority": "HIGH",
                "action": "Expand Skills",
                "description": f"Add {8 - skill_analysis['total_unique_skills']} more relevant skills",
                "steps": ["Research industry-standard tools", "Include technologies from job postings"]
            })
        
        # Check JD alignment
        if jd_analysis and jd_analysis.get("match_score"):
            if jd_analysis["match_score"] < 60:
                actions.append({
                    "priority": "HIGH",
                    "action": "Tailor to Job Description",
                    "description": "Resume doesn't align well with target role",
                    "steps": jd_analysis.get("recommendations", [])[:2]
                })
        
        return actions
    
    def _generate_insights(
        self,
        ats_results: Dict,
        role_matches: list,
        skill_analysis: Dict,
        experience: Dict
    ) -> list:
        """Generate actionable insights."""
        insights = []
        
        # ATS Insight
        insights.append({
            "category": "ATS Compatibility",
            "insight": f"Your resume scores {ats_results['grade']} for ATS systems",
            "impact": "HIGH" if ats_results["overall_score"] >= 75 else "CRITICAL",
            "detail": ats_results["feedback"]
        })
        
        # Role Fit Insight
        if role_matches:
            best_role = role_matches[0]
            insights.append({
                "category": "Best Role Fit",
                "insight": f"Strongest match: {best_role['role']} ({best_role['confidence']} confidence)",
                "impact": "MEDIUM",
                "detail": f"You have {best_role['match_count']['total']} relevant skills/tools"
            })
        
        # Skill Diversity Insight
        insights.append({
            "category": "Skill Portfolio",
            "insight": f"{skill_analysis['total_unique_skills']} unique skills identified",
            "impact": "MEDIUM",
            "detail": "Aim for 12-15 relevant skills for competitive roles"
        })
        
        # Experience Insight
        if experience.get("max_years", 0) > 0:
            insights.append({
                "category": "Experience Level",
                "insight": f"~{experience['max_years']} years of experience detected",
                "impact": "LOW",
                "detail": "Ensure experience descriptions showcase growth and impact"
            })
        
        return insights

# Singleton instance
resume_analysis_service = ResumeAnalysisService()