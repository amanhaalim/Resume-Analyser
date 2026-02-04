"""
Sample test script to test the Resume Analyzer API
"""

import requests 
import json
import time
from pathlib import Path

# Configuration
API_BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test health check endpoint."""
    print("\n" + "="*50)
    print("Testing Health Check Endpoint")
    print("="*50)
    
    response = requests.get(f"{API_BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    return response.status_code == 200

def test_get_categories():
    """Test get categories endpoint."""
    print("\n" + "="*50)
    print("Testing Get Categories Endpoint")
    print("="*50)
    
    response = requests.get(f"{API_BASE_URL}/categories")
    data = response.json()
    print(f"Status Code: {response.status_code}")
    print(f"Total Categories: {data.get('count')}")
    print(f"Categories: {', '.join(data.get('categories', []))}")
    
    return response.status_code == 200

def test_get_roles():
    """Test get roles endpoint."""
    print("\n" + "="*50)
    print("Testing Get Roles Endpoint")
    print("="*50)
    
    response = requests.get(f"{API_BASE_URL}/roles")
    data = response.json()
    print(f"Status Code: {response.status_code}")
    print(f"Total Roles: {data.get('count')}")
    print(f"Sample Roles: {', '.join(data.get('roles', [])[:5])}...")
    
    return response.status_code == 200

def test_get_role_details():
    """Test get role details endpoint."""
    print("\n" + "="*50)
    print("Testing Get Role Details Endpoint")
    print("="*50)
    
    role_name = "Data Scientist"
    response = requests.get(f"{API_BASE_URL}/roles/{role_name}")
    data = response.json()
    print(f"Status Code: {response.status_code}")
    print(f"Role: {data.get('role')}")
    print(f"Category: {data.get('details', {}).get('category')}")
    print(f"Skills: {', '.join(data.get('details', {}).get('skills', [])[:5])}...")
    
    return response.status_code == 200

def test_validate_resume(file_path):
    """Test validate endpoint."""
    print("\n" + "="*50)
    print("Testing Validate Resume Endpoint")
    print("="*50)
    
    if not Path(file_path).exists():
        print(f"File not found: {file_path}")
        return False
    
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{API_BASE_URL}/validate", files=files)
    
    data = response.json()
    print(f"Status Code: {response.status_code}")
    print(f"Valid: {data.get('valid')}")
    if not data.get('valid'):
        print(f"Error: {data.get('error')}")
    
    return response.status_code == 200

def test_analyze_resume(file_path, job_description=None):
    """Test analyze endpoint."""
    print("\n" + "="*50)
    print("Testing Analyze Resume Endpoint")
    print("="*50)
    
    if not Path(file_path).exists():
        print(f"File not found: {file_path}")
        return False
    
    start_time = time.time()
    
    with open(file_path, "rb") as f:
        files = {"file": f}
        data = {}
        
        if job_description:
            data["job_description"] = job_description
        
        response = requests.post(f"{API_BASE_URL}/analyze", files=files, data=data)
    
    elapsed_time = time.time() - start_time
    
    print(f"Status Code: {response.status_code}")
    print(f"Processing Time: {elapsed_time:.2f}s")
    
    if response.status_code == 200:
        result = response.json()
        
        if result.get('success'):
            data = result.get('data', {})
            
            # Resume Health
            health = data.get('resume_health', {})
            print(f"\n📊 Resume Health: {health.get('overall_score')}/100 - {health.get('status')}")
            
            # ATS Analysis
            ats = data.get('ats_analysis', {})
            print(f"\n🎯 ATS Score: {ats.get('overall_score')}/100 (Grade: {ats.get('grade')})")
            print(f"Feedback: {ats.get('feedback')}")
            
            # Skills
            skills_data = data.get('skills', {})
            print(f"\n💼 Skills Found: {skills_data.get('total_skills')}")
            print(f"Top Skills: {', '.join(skills_data.get('extracted_skills', [])[:10])}")
            
            # Role Matching
            role_match = data.get('role_matching', {})
            best_role = role_match.get('best_fit_role', {})
            if best_role:
                print(f"\n🎯 Best Role Match: {best_role.get('role')}")
                print(f"Score: {best_role.get('overall_score')}/100")
                print(f"Confidence: {best_role.get('confidence')}")
            
            # Top 3 matches
            print(f"\n📈 Top 3 Role Matches:")
            for i, role in enumerate(role_match.get('top_matches', [])[:3], 1):
                print(f"{i}. {role.get('role')} - {role.get('overall_score')}/100 ({role.get('confidence')})")
            
            # JD Match
            if job_description:
                jd_match = data.get('job_description_match', {})
                if jd_match:
                    print(f"\n📝 Job Description Match: {jd_match.get('match_score')}/100")
                    print(f"Grade: {jd_match.get('grade')}")
            
            # Recommendations
            recommendations = data.get('recommendations', {})
            overall_recs = recommendations.get('overall', [])
            if overall_recs:
                print(f"\n💡 Top Recommendations:")
                for i, rec in enumerate(overall_recs[:5], 1):
                    print(f"{i}. {rec}")
            
            # Save full response
            output_file = "analysis_result.json"
            with open(output_file, "w") as f:
                json.dump(result, f, indent=2)
            print(f"\n✅ Full analysis saved to: {output_file}")
            
            return True
        else:
            print(f"Error: {result.get('error')}")
            return False
    else:
        print(f"Error Response: {response.text}")
        return False

def test_statistics():
    """Test statistics endpoint."""
    print("\n" + "="*50)
    print("Testing Statistics Endpoint")
    print("="*50)
    
    response = requests.get(f"{API_BASE_URL}/stats")
    data = response.json()
    print(f"Status Code: {response.status_code}")
    
    if data.get('success'):
        stats = data.get('statistics', {})
        print(f"\n📊 System Statistics:")
        print(f"Total Roles: {stats.get('total_roles')}")
        print(f"Categories: {stats.get('total_categories')}")
        print(f"Skills Tracked: {stats.get('unique_skills_tracked')}")
        print(f"Tools Tracked: {stats.get('unique_tools_tracked')}")
        
        caps = data.get('capabilities', {})
        print(f"\n🔧 Capabilities:")
        print(f"File Formats: {', '.join(caps.get('file_formats', []))}")
        print(f"Analyses: {', '.join(caps.get('analyses', []))}")
    
    return response.status_code == 200

def run_all_tests(resume_file_path=None, job_description=None):
    """Run all tests."""
    print("\n" + "🚀"*25)
    print("Resume Analyzer Pro - API Testing Suite")
    print("🚀"*25)
    
    results = {}
    
    # Basic endpoint tests
    results['health'] = test_health_check()
    results['categories'] = test_get_categories()
    results['roles'] = test_get_roles()
    results['role_details'] = test_get_role_details()
    results['statistics'] = test_statistics()
    
    # File-based tests
    if resume_file_path:
        results['validate'] = test_validate_resume(resume_file_path)
        results['analyze'] = test_analyze_resume(resume_file_path, job_description)
    else:
        print("\n⚠️ No resume file provided. Skipping file-based tests.")
        print("Usage: python test_api.py <path_to_resume>")
    
    # Summary
    print("\n" + "="*50)
    print("Test Summary")
    print("="*50)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name.upper()}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    print("="*50)
    
    return passed == total

if __name__ == "__main__":
    import sys
    
    # Check if resume file path provided
    resume_path = sys.argv[1] if len(sys.argv) > 1 else None
    
    # Optional job description
    sample_jd = """
    We are seeking a Data Scientist with strong Python and Machine Learning skills.
    Requirements:
    - 3+ years of experience in data science
    - Proficiency in Python, SQL, and ML frameworks (scikit-learn, TensorFlow)
    - Experience with data visualization tools (Tableau, Power BI)
    - Strong statistical analysis and problem-solving skills
    - Bachelor's or Master's degree in Computer Science, Statistics, or related field
    """
    
    # Run tests
    success = run_all_tests(resume_path, sample_jd if resume_path else None)
    
    sys.exit(0 if success else 1)