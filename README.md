Resume_analyzer/

│
├── 📄 QUICKSTART.md              ← Start here! 5-minute setup guide

├── 📄 README.md                  ← Full documentation

├── 📄 DEPLOYMENT.md              ← Production deployment guide

│
├── 🐍 main.py                    ← FastAPI application (main entry point)

├── 🐍 config.py                  ← Configuration settings

├── 🐍 test_api.py                ← Test suite

│
├── 📦 requirements.txt           ← Python dependencies

├── 🐳 Dockerfile                 ← Docker container definition

├── 🐳 docker-compose.yml         ← Docker compose setup

├── 🔧 setup.sh                   ← Quick setup script

├── 📝 .gitignore                 ← Git ignore rules

│
├── 📂 data/

│   ├── __init__.py

│   └── 🎯 job_database.py        ← 100+ job roles database (31KB)
│
├── 📂 utils/

│   ├── __init__.py

│   ├── 🧠 skill_extractor.py     ← NLP-based skill extraction (9KB)

│   ├── 🎯 role_matcher.py        ← Intelligent role matching (10KB)

│   ├── 📊 ats_analyzer.py        ← ATS scoring engine (15KB)

│   └── 🔍 jd_matcher.py          ← Job description matcher (12KB)
│
└── 📂 services/

    ├── __init__.py
    
    ├── 📄 resume_parser.py       ← Multi-format parser (7KB)
    
    └── 🎛️ analysis_service.py    ← Main orchestration (12KB)


Resume AI Analyzer - Backend API
A production-ready, AI-powered resume analysis API with comprehensive job market coverage (100+ roles) and advanced ATS optimization.
🚀 Key Features
Comprehensive Analysis

100+ Job Roles across 15+ industries (Technology, Finance, Healthcare, Marketing, etc.)
Advanced ATS Scoring with industry-specific benchmarks
Intelligent Role Matching with confidence scoring
Skill Extraction with synonym detection and context awareness
Job Description Matching with semantic analysis
Quantifiable Metrics Detection to measure impact
Action Verb Analysis for compelling bullet points

Multi-Format Support

PDF documents
Microsoft Word (DOCX)
Plain text (TXT)
Images (PNG, JPG, JPEG) with OCR

Production-Ready

RESTful API with FastAPI
Comprehensive error handling
Request validation
Background task processing
CORS support
Auto-generated API documentation

📋 Prerequisites

Python 3.8 or higher
Tesseract OCR (for image processing)

Installing Tesseract
Ubuntu/Debian:
bashsudo apt-get update
sudo apt-get install tesseract-ocr
macOS:
bashbrew install tesseract
Windows:
Download installer from: https://github.com/UB-Mannheim/tesseract/wiki
🛠️ Installation
1. Clone/Download the project
bashcd resume_analyzer_pro
2. Create virtual environment
bashpython -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
3. Install dependencies
bashpip install -r requirements.txt
🚀 Running the API
Development Mode
bashuvicorn main:app --reload --host 0.0.0.0 --port 8000
Production Mode
bashgunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
The API will be available at: http://localhost:8000
📚 API Documentation
Once the server is running, visit:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

🔌 API Endpoints
Core Endpoints
1. Analyze Resume
httpPOST /analyze
Content-Type: multipart/form-data

Parameters:
- file: Resume file (PDF/DOCX/TXT/Image)
- job_description: (Optional) Job description text
- target_role: (Optional) Specific role to evaluate against
Example using cURL:
bashcurl -X POST "http://localhost:8000/analyze" \
  -F "file=@resume.pdf" \
  -F "job_description=We are looking for a Senior Data Scientist with Python and ML experience..."
Example using Python:
pythonimport requests

url = "http://localhost:8000/analyze"

with open("resume.pdf", "rb") as f:
    files = {"file": f}
    data = {
        "job_description": "Your job description here..."
    }
    response = requests.post(url, files=files, data=data)
    result = response.json()
    
print(f"ATS Score: {result['data']['ats_analysis']['overall_score']}")
print(f"Best Role: {result['data']['role_matching']['best_fit_role']['role']}")
2. Validate Resume
httpPOST /validate
Content-Type: multipart/form-data

Parameters:
- file: Resume file to validate
Quick validation without full analysis.
3. Get All Roles
httpGET /roles?category={category_name}
Returns list of all available job roles, optionally filtered by category.
4. Get Categories
httpGET /categories
Returns all industry categories.
5. Get Role Details
httpGET /roles/{role_name}
Get detailed information about a specific role including required skills, tools, and certifications.
6. System Statistics
httpGET /stats
Get system capabilities and statistics.
7. Health Check
httpGET /health
Check API health and service status.
📊 Response Structure
Analysis Response
json{
  "success": true,
  "data": {
    "resume_health": {
      "overall_score": 87.5,
      "status": "Excellent 🌟"
    },
    "ats_analysis": {
      "overall_score": 85.2,
      "grade": "A",
      "feedback": "Great! Your resume should pass most ATS systems.",
      "breakdown": {
        "sections": 23,
        "keywords": 18,
        "action_verbs": 14,
        "metrics": 18,
        "formatting": 8,
        "contact": 10
      },
      "suggestions": ["Add 'Projects' section...", ...],
      "strengths": ["✅ Contact: Strong (100%)", ...],
      "priority_improvements": []
    },
    "skills": {
      "extracted_skills": ["python", "sql", "machine learning", ...],
      "total_skills": 18,
      "high_confidence_skills": ["python", "sql", ...],
      "certifications": ["AWS Certified", ...]
    },
    "role_matching": {
      "top_matches": [
        {
          "role": "Data Scientist",
          "category": "Data & Analytics",
          "overall_score": 78.5,
          "confidence": "High",
          "breakdown": {
            "technical_skills": 80.0,
            "tools": 75.0,
            "soft_skills": 70.0
          },
          "matched_skills": {
            "technical": ["python", "machine learning", "sql"],
            "tools": ["jupyter", "git"]
          },
          "missing_skills": {
            "critical": ["r", "statistics"],
            "all": ["r", "statistics", "pandas", ...]
          },
          "insights": ["🎯 Excellent match for Data Scientist!", ...]
        }
      ],
      "best_fit_role": {...}
    },
    "job_description_match": {
      "match_score": 72.5,
      "grade": "B (Good Match)",
      "matched": {
        "skills": ["python", "sql", ...],
        "keywords": [...]
      },
      "missing": {
        "must_have_skills": ["spark", "hadoop"],
        "nice_to_have_skills": ["tableau"],
        "keywords": [...]
      },
      "recommendations": [...]
    },
    "recommendations": {
      "overall": [...],
      "priority_actions": [...]
    },
    "insights": [...]
  },
  "processing_time": 2.34,
  "timestamp": "2024-02-04T10:30:00"
}
🎯 Use Cases
1. Job Seeker Portal
Integrate this API to help job seekers:

Optimize resumes for ATS systems
Match their profile with suitable roles
Get actionable improvement suggestions
Tailor resumes for specific job descriptions

2. Recruitment Platform

Auto-screen candidates
Match candidates to open positions
Provide feedback to applicants
Reduce manual resume review time

3. Career Counseling

Assess student/client readiness
Identify skill gaps
Recommend career paths
Track improvement over time

4. Resume Builder Application

Real-time resume scoring
Live optimization suggestions
Role-specific templates
ATS compatibility checking

🏗️ Architecture
resume_analyzer_pro/
├── data/
│   ├── __init__.py
│   └── job_database.py          # 100+ roles database
├── utils/
│   ├── __init__.py
│   ├── skill_extractor.py       # NLP-based skill extraction
│   ├── role_matcher.py          # Intelligent role matching
│   ├── ats_analyzer.py          # ATS scoring engine
│   └── jd_matcher.py            # Job description matcher
├── services/
│   ├── __init__.py
│   ├── resume_parser.py         # Multi-format parser
│   └── analysis_service.py      # Main orchestration
├── main.py                       # FastAPI application
├── requirements.txt
└── README.md
🔧 Configuration
Environment Variables (Optional)
Create a .env file:
env# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4

# File Upload
MAX_UPLOAD_SIZE=10485760  # 10MB in bytes
ALLOWED_EXTENSIONS=pdf,docx,txt,png,jpg,jpeg

# CORS
CORS_ORIGINS=http://localhost:3000,https://yourfrontend.com
📈 Performance

Average analysis time: 2-4 seconds per resume
Supports concurrent requests
Efficient caching for repeated analyses
Background task processing for cleanup

🧪 Testing
bash# Run tests
pytest

# Test with sample resume
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@sample_resume.pdf"
🔒 Security Considerations

Implement rate limiting in production
Add authentication/authorization
Sanitize file uploads
Set up proper CORS policies
Use HTTPS in production
Implement request size limits

🚀 Deployment
Docker Deployment
Create Dockerfile:
dockerfileFROM python:3.11-slim

# Install Tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
Build and run:
bashdocker build -t resume-analyzer .
docker run -p 8000:8000 resume-analyzer
Cloud Deployment
Deploy to AWS, GCP, Azure, or platforms like:

Heroku
Railway
Render
DigitalOcean App Platform

📝 Advanced Features (Future Enhancements)

 Resume scoring history tracking
 A/B testing for resume variations
 Industry trend analysis
 Salary estimation
 Cover letter analysis
 LinkedIn profile optimization
 Multi-language support
 PDF resume generation
 Resume templates

🤝 Contributing
This is a production-ready backend. Customize as needed:

Add more roles to data/job_database.py
Enhance skill extraction in utils/skill_extractor.py
Improve scoring algorithms in utils/ats_analyzer.py
Add new endpoints in main.py

📄 License
MIT License - Feel free to use in commercial and personal projects
🆘 Support
For issues or questions:

Check API documentation at /docs
Review error messages in response
Check logs for detailed error traces

🎓 Key Improvements Over Original

Scalability: 10x more job roles (10 → 100+)
Intelligence: Advanced NLP-based skill extraction with context
Accuracy: Semantic matching with synonym detection
Depth: Industry-specific ATS benchmarks
Insights: Actionable, prioritized recommendations
Robustness: Comprehensive error handling and validation
Production-Ready: Proper API structure, documentation, testing

📊 Example Analysis Output
Resume Health: 87.5/100 (Excellent 🌟)
ATS Score: 85.2/100 (Grade A)

Top Role Matches:
1. Data Scientist - 78.5% (High Confidence)
2. Machine Learning Engineer - 72.3% (High Confidence)
3. Data Analyst - 68.9% (Medium Confidence)

Key Strengths:
✅ Strong technical skills (18 detected)
✅ Quantifiable achievements (12 metrics)
✅ Action-oriented language

Priority Improvements:
🔴 Add certifications to boost credibility
🟡 Include more soft skills
💡 Tailor keywords to job description
