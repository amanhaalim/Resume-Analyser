"""
Configuration settings for Resume Analyzer Pro
"""

import os
from typing import List

class Settings:
    """Application settings."""
    
    # API Settings
    API_TITLE: str = "Resume AI Analyzer Pro"
    API_VERSION: str = "2.0.0"
    API_DESCRIPTION: str = "Advanced AI-powered resume analysis with 100+ job roles coverage"
    
    # Server Settings
    HOST: str = os.getenv("API_HOST", "0.0.0.0")
    PORT: int = int(os.getenv("API_PORT", "8000"))
    WORKERS: int = int(os.getenv("API_WORKERS", "4"))
    
    # File Upload Settings
    UPLOAD_DIR: str = "uploads"
    MAX_UPLOAD_SIZE: int = int(os.getenv("MAX_UPLOAD_SIZE", "10485760"))  # 10MB
    ALLOWED_EXTENSIONS: List[str] = [".pdf", ".docx", ".doc", ".txt", ".png", ".jpg", ".jpeg"]
    
    # CORS Settings
    CORS_ORIGINS: List[str] = os.getenv(
        "CORS_ORIGINS", 
        "*"
    ).split(",")
    
    # Analysis Settings
    MIN_RESUME_LENGTH: int = 50
    MAX_SKILLS_TO_DISPLAY: int = 50
    TOP_ROLE_MATCHES: int = 10
    
    # Cache Settings (for future enhancement)
    ENABLE_CACHE: bool = os.getenv("ENABLE_CACHE", "false").lower() == "true"
    CACHE_TTL: int = int(os.getenv("CACHE_TTL", "3600"))  # 1 hour
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # Feature Flags
    ENABLE_OCR: bool = True
    ENABLE_JD_MATCHING: bool = True
    ENABLE_ROLE_INSIGHTS: bool = True
    
    @classmethod
    def create_upload_dir(cls):
        """Create upload directory if it doesn't exist."""
        os.makedirs(cls.UPLOAD_DIR, exist_ok=True)

settings = Settings()