"""
Advanced NLP-based skill extraction with semantic matching,
synonym detection, and context-aware extraction.
"""

import re
from typing import List, Dict, Set, Tuple
from collections import Counter
from data.job_database import JOB_DATABASE, SKILL_SYNONYMS

class SkillExtractor:
    def __init__(self):
        self.all_skills = self._build_skill_database()
        self.skill_patterns = self._build_skill_patterns()
        
    def _build_skill_database(self) -> Set[str]:
        """Build comprehensive skill database from all roles."""
        skills = set()
        for role_data in JOB_DATABASE.values():
            skills.update([s.lower() for s in role_data.get("skills", [])])
            skills.update([s.lower() for s in role_data.get("tools", [])])
            skills.update([s.lower() for s in role_data.get("soft_skills", [])])
        
        # Add synonyms
        for skill, synonyms in SKILL_SYNONYMS.items():
            skills.add(skill.lower())
            skills.update([s.lower() for s in synonyms])
        
        return skills
    
    def _build_skill_patterns(self) -> List[re.Pattern]:
        """Build regex patterns for skill extraction."""
        patterns = []
        
        # Sort skills by length (longest first) to match multi-word skills first
        sorted_skills = sorted(self.all_skills, key=len, reverse=True)
        
        for skill in sorted_skills:
            # Create pattern that matches skill with word boundaries
            pattern = r'\b' + re.escape(skill) + r'\b'
            patterns.append((skill, re.compile(pattern, re.IGNORECASE)))
        
        return patterns
    
    def extract_skills(self, text: str) -> Dict[str, any]:
        """Extract skills from text with context and confidence."""
        text_lower = text.lower()
        
        # Extract skills
        found_skills = {}
        skill_contexts = []
        
        for skill, pattern in self.skill_patterns:
            matches = pattern.finditer(text_lower)
            for match in matches:
                # Get context around the skill (50 chars before and after)
                start = max(0, match.start() - 50)
                end = min(len(text), match.end() + 50)
                context = text[start:end].strip()
                
                # Normalize skill using synonyms
                normalized_skill = self._normalize_skill(skill)
                
                if normalized_skill not in found_skills:
                    found_skills[normalized_skill] = {
                        "count": 0,
                        "contexts": [],
                        "confidence": 0.0
                    }
                
                found_skills[normalized_skill]["count"] += 1
                if len(found_skills[normalized_skill]["contexts"]) < 3:
                    found_skills[normalized_skill]["contexts"].append(context)
        
        # Calculate confidence scores
        for skill, data in found_skills.items():
            # Higher confidence for more mentions and skills in certain sections
            base_confidence = min(data["count"] * 0.2, 1.0)
            
            # Boost confidence if skill appears in skills section
            section_boost = 0.0
            for context in data["contexts"]:
                if any(keyword in context.lower() for keyword in ["skills", "technologies", "tools", "expertise"]):
                    section_boost = 0.3
                    break
            
            data["confidence"] = min(base_confidence + section_boost, 1.0)
        
        # Sort by confidence and count
        sorted_skills = sorted(
            found_skills.items(),
            key=lambda x: (x[1]["confidence"], x[1]["count"]),
            reverse=True
        )
        
        return {
            "skills": dict(sorted_skills),
            "skill_list": [s for s, _ in sorted_skills],
            "total_unique_skills": len(sorted_skills),
            "high_confidence_skills": [s for s, d in sorted_skills if d["confidence"] > 0.7]
        }
    
    def _normalize_skill(self, skill: str) -> str:
        """Normalize skill using synonym mapping."""
        skill_lower = skill.lower()
        
        # Check if this skill is a synonym of a primary skill
        for primary, synonyms in SKILL_SYNONYMS.items():
            if skill_lower == primary or skill_lower in [s.lower() for s in synonyms]:
                return primary
        
        return skill_lower
    
    def extract_certifications(self, text: str) -> List[str]:
        """Extract certifications and credentials."""
        cert_patterns = [
            r'\b(AWS|Azure|GCP|Google Cloud)\s+Certified\s+\w+',
            r'\b(PMP|CISSP|CEH|OSCP|Security\+|Network\+|A\+)',
            r'\b(CPA|CFA|CMA|SHRM-CP|SHRM-SCP|PHR|SPHR)',
            r'\b(Scrum Master|Product Owner|SAFe|Prince2)',
            r'\b(Six Sigma|Black Belt|Green Belt)',
            r'\b(Certified|Certification)\s+\w+',
        ]
        
        certifications = set()
        for pattern in cert_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    cert = ' '.join(filter(None, match))
                else:
                    cert = match
                certifications.add(cert)
        
        return sorted(list(certifications))
    
    def extract_years_of_experience(self, text: str) -> Dict[str, int]:
        """Extract years of experience from text."""
        # Patterns for experience
        patterns = [
            r'(\d+)\+?\s*years?\s+(?:of\s+)?experience',
            r'experience\s+(?:of\s+)?(\d+)\+?\s*years?',
            r'(\d+)\+?\s*years?\s+(?:working|in)',
        ]
        
        years = []
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            years.extend([int(m) for m in matches])
        
        if years:
            return {
                "max_years": max(years),
                "min_years": min(years),
                "avg_years": sum(years) // len(years)
            }
        
        return {"max_years": 0, "min_years": 0, "avg_years": 0}
    
    def extract_education(self, text: str) -> List[Dict[str, str]]:
        """Extract education information."""
        education = []
        
        # Degree patterns
        degree_patterns = [
            r'\b(Bachelor|BS|BA|B\.S\.|B\.A\.)\s+(?:of\s+)?(?:Science|Arts)?\s+in\s+([A-Za-z\s]+)',
            r'\b(Master|MS|MA|M\.S\.|M\.A\.|MBA)\s+(?:of\s+)?(?:Science|Arts|Business)?\s+in\s+([A-Za-z\s]+)',
            r'\b(Ph\.?D\.?|Doctorate)\s+in\s+([A-Za-z\s]+)',
            r'\b(Associate|AS|AA)\s+(?:of\s+)?(?:Science|Arts)?\s+in\s+([A-Za-z\s]+)',
        ]
        
        for pattern in degree_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                degree_type = match[0]
                major = match[1].strip() if len(match) > 1 else "Unknown"
                education.append({
                    "degree": degree_type,
                    "major": major
                })
        
        return education
    
    def extract_action_verbs(self, text: str) -> List[Dict[str, any]]:
        """Extract action verbs and their usage."""
        action_verbs = [
            "built", "developed", "designed", "implemented", "optimized", "analyzed",
            "created", "automated", "deployed", "improved", "engineered", "trained",
            "led", "managed", "coordinated", "established", "launched", "delivered",
            "architected", "scaled", "maintained", "integrated", "migrated", "streamlined",
            "reduced", "increased", "achieved", "collaborated", "spearheaded", "pioneered"
        ]
        
        verb_usage = []
        text_lower = text.lower()
        
        for verb in action_verbs:
            pattern = r'\b' + verb + r'\b'
            matches = re.finditer(pattern, text_lower)
            count = len(list(matches))
            
            if count > 0:
                verb_usage.append({
                    "verb": verb,
                    "count": count
                })
        
        return sorted(verb_usage, key=lambda x: x["count"], reverse=True)
    
    def extract_metrics(self, text: str) -> List[Dict[str, str]]:
        """Extract quantifiable metrics and achievements."""
        metric_patterns = [
            r'(\d+(?:\.\d+)?%)\s+(?:increase|decrease|improvement|reduction|growth)',
            r'(?:increased|decreased|improved|reduced|grew)\s+(?:by\s+)?(\d+(?:\.\d+)?%)',
            r'\$(\d+(?:,\d{3})*(?:\.\d+)?)\s*(?:million|billion|thousand|M|B|K)?',
            r'(\d+(?:,\d{3})*)\s+(?:users|customers|clients|projects|features|products)',
            r'(?:from|to)\s+(\d+(?:,\d{3})*)',
        ]
        
        metrics = []
        for pattern in metric_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                # Get context
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                context = text[start:end].strip()
                
                metrics.append({
                    "metric": match.group(0),
                    "context": context
                })
        
        return metrics[:10]  # Return top 10 metrics

skill_extractor = SkillExtractor()