"""
Advanced ATS (Applicant Tracking System) Analyzer
- Industry-specific scoring
- Section analysis
- Formatting checks
- Keyword density
- Action verb usage
- Quantifiable achievements
"""

import re
from typing import Dict, List, Tuple
from collections import Counter

class ATSAnalyzer:
    def __init__(self):
        self.section_keywords = {
            "contact": ["email", "phone", "linkedin", "github", "portfolio"],
            "summary": ["summary", "profile", "objective", "about"],
            "experience": ["experience", "work history", "employment", "professional experience"],
            "education": ["education", "academic", "degree", "university", "college"],
            "skills": ["skills", "technical skills", "core competencies", "expertise"],
            "projects": ["projects", "portfolio", "key projects"],
            "certifications": ["certifications", "licenses", "credentials"],
            "awards": ["awards", "honors", "achievements", "recognition"],
        }
        
        self.action_verbs = {
            "leadership": ["led", "managed", "directed", "supervised", "coordinated", "headed", "spearheaded"],
            "achievement": ["achieved", "accomplished", "delivered", "exceeded", "surpassed", "completed"],
            "creation": ["built", "created", "developed", "designed", "established", "founded", "launched"],
            "improvement": ["improved", "optimized", "enhanced", "streamlined", "reduced", "increased"],
            "technical": ["implemented", "engineered", "deployed", "integrated", "migrated", "automated"],
            "analysis": ["analyzed", "evaluated", "assessed", "researched", "investigated", "identified"],
            "collaboration": ["collaborated", "partnered", "cooperated", "contributed", "facilitated"]
        }
        
        self.formatting_keywords = [
            "professional", "clean", "organized", "structured", "clear"
        ]
    
    def analyze_ats_score(
        self,
        text: str,
        extracted_skills: List[str],
        sections_found: Dict[str, bool],
        action_verbs: List[Dict],
        metrics: List[Dict]
    ) -> Dict:
        """
        Comprehensive ATS scoring with detailed breakdown.
        """
        
        scores = {}
        suggestions = []
        
        # 1. Section Completeness (25 points)
        section_score, section_suggestions = self._score_sections(sections_found)
        scores["sections"] = section_score
        suggestions.extend(section_suggestions)
        
        # 2. Keyword Optimization (20 points)
        keyword_score, keyword_suggestions = self._score_keywords(text, extracted_skills)
        scores["keywords"] = keyword_score
        suggestions.extend(keyword_suggestions)
        
        # 3. Action Verbs (15 points)
        verb_score, verb_suggestions = self._score_action_verbs(text, action_verbs)
        scores["action_verbs"] = verb_score
        suggestions.extend(verb_suggestions)
        
        # 4. Quantifiable Achievements (20 points)
        metrics_score, metrics_suggestions = self._score_metrics(metrics, text)
        scores["metrics"] = metrics_score
        suggestions.extend(metrics_suggestions)
        
        # 5. Formatting & Length (10 points)
        format_score, format_suggestions = self._score_formatting(text)
        scores["formatting"] = format_score
        suggestions.extend(format_suggestions)
        
        # 6. Contact Information (10 points)
        contact_score, contact_suggestions = self._score_contact_info(text)
        scores["contact"] = contact_score
        suggestions.extend(contact_suggestions)
        
        # Calculate overall ATS score
        overall_score = sum(scores.values())
        
        # Grade and feedback
        grade, feedback = self._get_grade_and_feedback(overall_score)
        
        return {
            "overall_score": round(overall_score, 2),
            "grade": grade,
            "feedback": feedback,
            "breakdown": scores,
            "suggestions": suggestions[:15],  # Top 15 suggestions
            "strengths": self._identify_strengths(scores),
            "priority_improvements": self._identify_priorities(scores, suggestions)
        }
    
    def _score_sections(self, sections: Dict[str, bool]) -> Tuple[float, List[str]]:
        """Score section completeness."""
        required_sections = ["experience", "education", "skills"]
        recommended_sections = ["summary", "projects", "certifications"]
        
        score = 0.0
        suggestions = []
        
        # Required sections (15 points)
        required_present = sum(1 for s in required_sections if sections.get(s, False))
        score += (required_present / len(required_sections)) * 15
        
        # Recommended sections (10 points)
        recommended_present = sum(1 for s in recommended_sections if sections.get(s, False))
        score += (recommended_present / len(recommended_sections)) * 10
        
        # Suggestions
        for section in required_sections:
            if not sections.get(section, False):
                suggestions.append(f"⚠️ CRITICAL: Add '{section.title()}' section - required by most ATS systems.")
        
        for section in recommended_sections:
            if not sections.get(section, False):
                suggestions.append(f"💡 Add '{section.title()}' section to strengthen your resume.")
        
        return score, suggestions
    
    def _score_keywords(self, text: str, skills: List[str]) -> Tuple[float, List[str]]:
        """Score keyword optimization."""
        score = 0.0
        suggestions = []
        
        # Skill count (10 points)
        skill_count = len(skills)
        if skill_count >= 15:
            score += 10
        elif skill_count >= 10:
            score += 7
        elif skill_count >= 5:
            score += 4
        else:
            suggestions.append("⚠️ Add more relevant technical skills - aim for 10-15 skills.")
        
        # Keyword density (10 points)
        word_count = len(text.split())
        if word_count > 0:
            keyword_density = (skill_count * 3) / word_count  # Rough estimate
            if keyword_density >= 0.05:
                score += 10
            elif keyword_density >= 0.03:
                score += 7
            elif keyword_density >= 0.01:
                score += 4
            else:
                suggestions.append("💡 Increase keyword density by mentioning skills in context.")
        
        if skill_count < 8:
            suggestions.append(f"Add {8 - skill_count} more relevant skills to improve ATS match.")
        
        return score, suggestions
    
    def _score_action_verbs(self, text: str, action_verbs: List[Dict]) -> Tuple[float, List[str]]:
        """Score action verb usage."""
        score = 0.0
        suggestions = []
        
        text_lower = text.lower()
        
        # Count unique action verbs used
        unique_verbs = len(action_verbs)
        total_verb_usage = sum(v["count"] for v in action_verbs)
        
        # Diversity score (7 points)
        if unique_verbs >= 10:
            score += 7
        elif unique_verbs >= 6:
            score += 5
        elif unique_verbs >= 3:
            score += 3
        else:
            suggestions.append("⚠️ Use more diverse action verbs - aim for 10+ different verbs.")
        
        # Frequency score (8 points)
        if total_verb_usage >= 15:
            score += 8
        elif total_verb_usage >= 10:
            score += 5
        elif total_verb_usage >= 5:
            score += 3
        else:
            suggestions.append("💡 Start more bullet points with strong action verbs.")
        
        # Check for weak phrases
        weak_phrases = ["responsible for", "duties include", "tasks include"]
        for phrase in weak_phrases:
            if phrase in text_lower:
                suggestions.append(f"❌ Replace '{phrase}' with action verbs like 'Led', 'Developed', 'Managed'.")
        
        if unique_verbs < 8:
            suggestions.append("💡 Example strong verbs: Architected, Spearheaded, Optimized, Pioneered")
        
        return score, suggestions
    
    def _score_metrics(self, metrics: List[Dict], text: str) -> Tuple[float, List[str]]:
        """Score quantifiable achievements."""
        score = 0.0
        suggestions = []
        
        metric_count = len(metrics)
        
        # Quantity score (15 points)
        if metric_count >= 8:
            score += 15
        elif metric_count >= 5:
            score += 10
        elif metric_count >= 3:
            score += 6
        elif metric_count >= 1:
            score += 3
        else:
            suggestions.append("⚠️ CRITICAL: Add quantifiable metrics to demonstrate impact.")
        
        # Quality check (5 points)
        has_percentages = any('%' in m["metric"] for m in metrics)
        has_numbers = any(re.search(r'\d{2,}', m["metric"]) for m in metrics)
        has_currency = any('$' in m["metric"] for m in metrics)
        
        quality_count = sum([has_percentages, has_numbers, has_currency])
        score += (quality_count / 3) * 5
        
        # Suggestions
        if metric_count < 5:
            suggestions.append("💡 Add numbers: '20% improvement', '$50K savings', '1000+ users'")
        
        if not has_percentages:
            suggestions.append("💡 Include percentage improvements (e.g., 'reduced time by 30%')")
        
        if metric_count == 0:
            suggestions.append("⚠️ Example: 'Increased sales by 25%, managing $2M portfolio'")
        
        return score, suggestions
    
    def _score_formatting(self, text: str) -> Tuple[float, List[str]]:
        """Score formatting and length."""
        score = 0.0
        suggestions = []
        
        word_count = len(text.split())
        
        # Optimal length (5 points)
        if 400 <= word_count <= 1000:
            score += 5
        elif 300 <= word_count <= 1200:
            score += 3
        elif word_count < 300:
            suggestions.append("⚠️ Resume seems too short - add more details about projects and experience.")
        else:
            suggestions.append("💡 Consider condensing - resumes should be concise (400-1000 words).")
        
        # Bullet point structure (5 points)
        bullet_patterns = [r'•', r'-', r'►', r'→', r'\*']
        has_bullets = any(re.search(pattern, text) for pattern in bullet_patterns)
        
        if has_bullets:
            score += 5
        else:
            suggestions.append("💡 Use bullet points for better readability and ATS parsing.")
        
        return score, suggestions
    
    def _score_contact_info(self, text: str) -> Tuple[float, List[str]]:
        """Score contact information completeness."""
        score = 0.0
        suggestions = []
        
        # Email (3 points)
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.search(email_pattern, text):
            score += 3
        else:
            suggestions.append("⚠️ Include email address in contact section.")
        
        # Phone (2 points)
        phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        if re.search(phone_pattern, text):
            score += 2
        else:
            suggestions.append("💡 Include phone number for contact.")
        
        # LinkedIn (3 points)
        if 'linkedin' in text.lower():
            score += 3
        else:
            suggestions.append("💡 Add LinkedIn profile URL.")
        
        # GitHub/Portfolio (2 points)
        if 'github' in text.lower() or 'portfolio' in text.lower():
            score += 2
        else:
            suggestions.append("💡 Include GitHub or portfolio link to showcase work.")
        
        return score, suggestions
    
    def _get_grade_and_feedback(self, score: float) -> Tuple[str, str]:
        """Get letter grade and feedback."""
        if score >= 90:
            return "A+", "Excellent! Your resume is highly optimized for ATS systems."
        elif score >= 85:
            return "A", "Great! Your resume should pass most ATS systems."
        elif score >= 80:
            return "A-", "Very good! Minor improvements will maximize your chances."
        elif score >= 75:
            return "B+", "Good! Some enhancements needed for optimal ATS performance."
        elif score >= 70:
            return "B", "Decent. Address key suggestions to improve ATS compatibility."
        elif score >= 65:
            return "B-", "Fair. Important improvements needed."
        elif score >= 60:
            return "C+", "Below average. Significant improvements required."
        elif score >= 55:
            return "C", "Poor. Major revisions needed for ATS success."
        else:
            return "D", "Critical issues detected. Complete restructuring recommended."
    
    def _identify_strengths(self, scores: Dict[str, float]) -> List[str]:
        """Identify resume strengths."""
        strengths = []
        
        for category, score in scores.items():
            max_score = self._get_max_score(category)
            percentage = (score / max_score) * 100 if max_score > 0 else 0
            
            if percentage >= 80:
                strengths.append(f"✅ {category.replace('_', ' ').title()}: Strong ({percentage:.0f}%)")
        
        return strengths if strengths else ["Keep working on improving all areas!"]
    
    def _identify_priorities(self, scores: Dict[str, float], suggestions: List[str]) -> List[str]:
        """Identify priority improvements."""
        priorities = []
        
        for category, score in scores.items():
            max_score = self._get_max_score(category)
            percentage = (score / max_score) * 100 if max_score > 0 else 0
            
            if percentage < 50:
                priorities.append(f"🔴 URGENT: {category.replace('_', ' ').title()} ({percentage:.0f}%)")
            elif percentage < 70:
                priorities.append(f"🟡 Important: {category.replace('_', ' ').title()} ({percentage:.0f}%)")
        
        return priorities[:5] if priorities else ["Great job! Focus on minor refinements."]
    
    def _get_max_score(self, category: str) -> float:
        """Get maximum score for each category."""
        max_scores = {
            "sections": 25,
            "keywords": 20,
            "action_verbs": 15,
            "metrics": 20,
            "formatting": 10,
            "contact": 10
        }
        return max_scores.get(category, 0)
    
    def detect_sections(self, text: str) -> Dict[str, bool]:
        """Detect which sections are present in the resume."""
        sections_found = {}
        text_lower = text.lower()
        
        for section, keywords in self.section_keywords.items():
            sections_found[section] = any(keyword in text_lower for keyword in keywords)
        
        return sections_found

ats_analyzer = ATSAnalyzer()