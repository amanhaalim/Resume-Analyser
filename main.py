"""
Production-Ready Resume Analyzer API
Comprehensive backend with advanced analysis capabilities.
"""

from fastapi import FastAPI, UploadFile, File, Form, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
import os
import shutil
import time
from datetime import datetime

from services.resume_parser import resume_parser
from services.analysis_service import resume_analysis_service
from data.job_database import get_all_roles, get_all_categories, get_roles_by_category

# Initialize FastAPI app
app = FastAPI(
    title="Resume AI Analyzer Pro",
    description="Advanced AI-powered resume analysis with 100+ job roles coverage",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Upload directory
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Request/Response Models
class AnalysisResponse(BaseModel):
    """Response model for resume analysis."""
    success: bool
    data: Optional[dict] = None
    error: Optional[str] = None
    processing_time: Optional[float] = None
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())

class RoleInfo(BaseModel):
    """Model for role information."""
    role_name: str
    category: str
    required_skills: List[str]
    required_tools: List[str]
    certifications: List[str]

# Health check endpoint
@app.get("/", tags=["Health"])
def root():
    """Health check endpoint."""
    return {
        "status": "online",
        "service": "Resume Analyzer Pro API",
        "version": "2.0.0",
        "endpoints": {
            "analyze": "/analyze",
            "roles": "/roles",
            "categories": "/categories",
            "health": "/health"
        }
    }

@app.get("/health", tags=["Health"])
def health_check():
    """Detailed health check."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "services": {
            "parser": "operational",
            "analyzer": "operational",
            "role_matcher": "operational",
            "ats_scorer": "operational"
        },
        "database": {
            "total_roles": len(get_all_roles()),
            "categories": len(get_all_categories())
        }
    }

# Main analysis endpoint
@app.post("/analyze", response_model=AnalysisResponse, tags=["Analysis"])
async def analyze_resume(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(..., description="Resume file (PDF, DOCX, TXT, or Image)"),
    job_description: Optional[str] = Form(None, description="Optional job description for matching"),
    target_role: Optional[str] = Form(None, description="Optional target role name")
):
    """
    Comprehensive resume analysis endpoint.
    
    Supports:
    - PDF, DOCX, TXT, and Image formats
    - Optional job description matching
    - Optional target role evaluation
    
    Returns detailed analysis including:
    - ATS score and optimization suggestions
    - Role matching across 100+ positions
    - Skill extraction and assessment
    - Job description alignment (if provided)
    - Actionable recommendations
    """
    start_time = time.time()
    file_path = None
    
    try:
        # Validate file
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file provided")
        
        # Save uploaded file
        file_path = os.path.join(UPLOAD_DIR, f"{int(time.time())}_{file.filename}")
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Extract text from resume
        extracted_text, parse_error = resume_parser.extract_text(file_path, file.filename)
        
        if parse_error:
            raise HTTPException(status_code=400, detail=parse_error)
        
        # Validate resume content
        is_valid, validation_error = resume_parser.validate_resume(extracted_text)
        if not is_valid:
            raise HTTPException(status_code=400, detail=validation_error)
        
        # Perform comprehensive analysis
        analysis_result = resume_analysis_service.analyze_resume(
            resume_text=extracted_text,
            job_description=job_description if job_description else None,
            target_role=target_role if target_role else None
        )
        
        # Add metadata
        analysis_result["metadata"] = {
            "filename": file.filename,
            "file_size_kb": round(os.path.getsize(file_path) / 1024, 2),
            "text_length": len(extracted_text),
            "word_count": len(extracted_text.split()),
            "analyzed_at": datetime.now().isoformat()
        }
        
        # Schedule cleanup
        background_tasks.add_task(cleanup_file, file_path)
        
        processing_time = time.time() - start_time
        
        return AnalysisResponse(
            success=True,
            data=analysis_result,
            processing_time=round(processing_time, 2)
        )
        
    except HTTPException as he:
        # Cleanup on error
        if file_path and os.path.exists(file_path):
            background_tasks.add_task(cleanup_file, file_path)
        raise he
        
    except Exception as e:
        # Cleanup on error
        if file_path and os.path.exists(file_path):
            background_tasks.add_task(cleanup_file, file_path)
        
        return AnalysisResponse(
            success=False,
            error=f"Analysis failed: {str(e)}",
            processing_time=time.time() - start_time
        )

# Role information endpoints
@app.get("/roles", tags=["Roles"])
def get_roles(category: Optional[str] = None):
    """
    Get all available job roles.
    
    Optional query parameter:
    - category: Filter roles by industry category
    """
    try:
        if category:
            roles = get_roles_by_category(category)
            return {
                "success": True,
                "category": category,
                "count": len(roles),
                "roles": roles
            }
        else:
            all_roles = get_all_roles()
            return {
                "success": True,
                "count": len(all_roles),
                "roles": all_roles
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/categories", tags=["Roles"])
def get_categories():
    """Get all available industry categories."""
    try:
        categories = get_all_categories()
        return {
            "success": True,
            "count": len(categories),
            "categories": sorted(categories)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/roles/{role_name}", tags=["Roles"])
def get_role_details(role_name: str):
    """
    Get detailed information about a specific role.
    
    Path parameter:
    - role_name: Name of the role (e.g., "Data Scientist")
    """
    try:
        from data.job_database import JOB_DATABASE
        
        if role_name not in JOB_DATABASE:
            raise HTTPException(status_code=404, detail=f"Role '{role_name}' not found")
        
        role_data = JOB_DATABASE[role_name]
        
        return {
            "success": True,
            "role": role_name,
            "details": role_data
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Quick validation endpoint
@app.post("/validate", tags=["Validation"])
async def validate_resume_file(
    file: UploadFile = File(..., description="Resume file to validate")
):
    """
    Quick validation of resume file without full analysis.
    Checks if file can be parsed and contains resume-like content.
    """
    file_path = None
    
    try:
        # Save temporarily
        file_path = os.path.join(UPLOAD_DIR, f"temp_{int(time.time())}_{file.filename}")
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Extract and validate
        extracted_text, parse_error = resume_parser.extract_text(file_path, file.filename)
        
        if parse_error:
            return {
                "success": False,
                "valid": False,
                "error": parse_error
            }
        
        is_valid, validation_error = resume_parser.validate_resume(extracted_text)
        
        return {
            "success": True,
            "valid": is_valid,
            "error": validation_error if not is_valid else None,
            "preview": extracted_text[:500] if is_valid else None
        }
        
    except Exception as e:
        return {
            "success": False,
            "valid": False,
            "error": str(e)
        }
    finally:
        # Cleanup
        if file_path and os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass

# Statistics endpoint
@app.get("/stats", tags=["Statistics"])
def get_statistics():
    """Get system statistics and capabilities."""
    from data.job_database import JOB_DATABASE, SKILL_SYNONYMS
    
    total_skills = set()
    total_tools = set()
    total_certs = set()
    
    for role_data in JOB_DATABASE.values():
        total_skills.update(role_data.get("skills", []))
        total_tools.update(role_data.get("tools", []))
        total_certs.update(role_data.get("certifications", []))
    
    return {
        "success": True,
        "statistics": {
            "total_roles": len(JOB_DATABASE),
            "total_categories": len(get_all_categories()),
            "unique_skills_tracked": len(total_skills),
            "unique_tools_tracked": len(total_tools),
            "certifications_recognized": len(total_certs),
            "skill_synonyms": len(SKILL_SYNONYMS)
        },
        "capabilities": {
            "file_formats": ["PDF", "DOCX", "TXT", "PNG", "JPG", "JPEG"],
            "analyses": [
                "ATS Scoring",
                "Role Matching",
                "Skill Extraction",
                "Job Description Matching",
                "Action Verb Analysis",
                "Metrics Detection",
                "Section Analysis"
            ]
        }
    }

# Utility function for cleanup
def cleanup_file(file_path: str):
    """Background task to cleanup uploaded files."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception:
        pass  # Fail silently

# Error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "error": "Endpoint not found",
            "path": str(request.url)
        }
    )

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal server error",
            "message": str(exc)
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)