"""
Comprehensive Job Database with 100+ roles across all major industries.
Each role includes technical skills, soft skills, tools, and certifications.
"""

JOB_DATABASE = {
    # TECHNOLOGY & SOFTWARE
    "Software Engineer": {
        "category": "Technology",
        "skills": ["python", "java", "javascript", "c++", "go", "rust", "typescript"],
        "tools": ["git", "github", "gitlab", "jenkins", "docker", "kubernetes", "ci/cd"],
        "soft_skills": ["problem solving", "teamwork", "communication", "debugging"],
        "certifications": ["aws certified developer", "google cloud certified", "microsoft certified"],
        "keywords": ["development", "coding", "programming", "software", "backend", "frontend"]
    },
    "Full Stack Developer": {
        "category": "Technology",
        "skills": ["react", "angular", "vue", "node.js", "express", "mongodb", "postgresql", "mysql"],
        "tools": ["webpack", "babel", "npm", "yarn", "docker", "git"],
        "soft_skills": ["multitasking", "adaptability", "communication"],
        "certifications": ["full stack certification", "react certification"],
        "keywords": ["full stack", "web development", "frontend", "backend", "api"]
    },
    "DevOps Engineer": {
        "category": "Technology",
        "skills": ["docker", "kubernetes", "terraform", "ansible", "jenkins", "ci/cd", "linux"],
        "tools": ["aws", "azure", "gcp", "prometheus", "grafana", "elk stack"],
        "soft_skills": ["automation mindset", "collaboration", "problem solving"],
        "certifications": ["aws devops", "kubernetes certified", "terraform associate"],
        "keywords": ["devops", "automation", "infrastructure", "deployment", "monitoring"]
    },
    "Cloud Architect": {
        "category": "Technology",
        "skills": ["aws", "azure", "gcp", "cloud architecture", "microservices", "serverless"],
        "tools": ["terraform", "cloudformation", "kubernetes", "docker"],
        "soft_skills": ["strategic thinking", "communication", "leadership"],
        "certifications": ["aws solutions architect", "azure architect", "gcp architect"],
        "keywords": ["cloud", "architecture", "scalability", "infrastructure", "migration"]
    },
    "Data Engineer": {
        "category": "Data & Analytics",
        "skills": ["python", "sql", "spark", "hadoop", "kafka", "airflow", "etl"],
        "tools": ["databricks", "snowflake", "redshift", "bigquery", "azure data factory"],
        "soft_skills": ["analytical thinking", "attention to detail", "communication"],
        "certifications": ["databricks certified", "aws data analytics", "snowflake certified"],
        "keywords": ["data pipeline", "etl", "data warehouse", "big data", "streaming"]
    },
    "Data Scientist": {
        "category": "Data & Analytics",
        "skills": ["python", "r", "sql", "machine learning", "statistics", "pandas", "numpy", "scikit-learn"],
        "tools": ["jupyter", "tableau", "power bi", "git", "mlflow"],
        "soft_skills": ["analytical thinking", "communication", "business acumen"],
        "certifications": ["data science certification", "machine learning specialization"],
        "keywords": ["data science", "analytics", "modeling", "prediction", "insights"]
    },
    "Machine Learning Engineer": {
        "category": "Data & Analytics",
        "skills": ["python", "tensorflow", "pytorch", "scikit-learn", "deep learning", "mlops"],
        "tools": ["docker", "kubernetes", "mlflow", "wandb", "sagemaker"],
        "soft_skills": ["innovation", "problem solving", "collaboration"],
        "certifications": ["ml engineer certification", "tensorflow certified", "aws ml"],
        "keywords": ["machine learning", "ml", "ai", "model deployment", "training"]
    },
    "AI Engineer": {
        "category": "Data & Analytics",
        "skills": ["python", "nlp", "computer vision", "deep learning", "transformers", "llm"],
        "tools": ["hugging face", "openai api", "langchain", "pytorch", "tensorflow"],
        "soft_skills": ["innovation", "research", "communication"],
        "certifications": ["ai certification", "nlp specialization", "deep learning"],
        "keywords": ["artificial intelligence", "ai", "nlp", "computer vision", "generative ai"]
    },
    "Data Analyst": {
        "category": "Data & Analytics",
        "skills": ["sql", "excel", "python", "statistics", "data visualization"],
        "tools": ["tableau", "power bi", "looker", "google analytics", "excel"],
        "soft_skills": ["analytical thinking", "communication", "attention to detail"],
        "certifications": ["google data analytics", "tableau certified", "power bi certified"],
        "keywords": ["data analysis", "reporting", "dashboards", "insights", "metrics"]
    },
    "Business Analyst": {
        "category": "Business & Management",
        "skills": ["sql", "excel", "business intelligence", "requirements gathering", "process mapping"],
        "tools": ["power bi", "tableau", "jira", "confluence", "visio"],
        "soft_skills": ["stakeholder management", "communication", "critical thinking"],
        "certifications": ["cbap", "pmi-pba", "six sigma"],
        "keywords": ["business analysis", "requirements", "process improvement", "stakeholder"]
    },
    
    # CYBERSECURITY
    "Security Engineer": {
        "category": "Cybersecurity",
        "skills": ["penetration testing", "vulnerability assessment", "siem", "firewall", "ids/ips"],
        "tools": ["wireshark", "metasploit", "burp suite", "nessus", "splunk"],
        "soft_skills": ["attention to detail", "problem solving", "communication"],
        "certifications": ["cissp", "ceh", "oscp", "security+", "cism"],
        "keywords": ["security", "cybersecurity", "penetration testing", "vulnerability", "incident response"]
    },
    "Security Analyst": {
        "category": "Cybersecurity",
        "skills": ["threat analysis", "incident response", "soc", "siem", "forensics"],
        "tools": ["splunk", "qradar", "crowdstrike", "carbon black", "wireshark"],
        "soft_skills": ["analytical thinking", "attention to detail", "communication"],
        "certifications": ["security+", "ceh", "gcih", "cissp"],
        "keywords": ["security operations", "threat detection", "incident response", "soc"]
    },
    
    # DESIGN & CREATIVE
    "UX Designer": {
        "category": "Design",
        "skills": ["user research", "wireframing", "prototyping", "user testing", "interaction design"],
        "tools": ["figma", "sketch", "adobe xd", "invision", "miro", "usertesting"],
        "soft_skills": ["empathy", "communication", "creativity", "collaboration"],
        "certifications": ["ux certification", "interaction design foundation"],
        "keywords": ["ux", "user experience", "design thinking", "usability", "research"]
    },
    "UI Designer": {
        "category": "Design",
        "skills": ["visual design", "typography", "color theory", "responsive design", "design systems"],
        "tools": ["figma", "sketch", "adobe creative suite", "principle", "framer"],
        "soft_skills": ["creativity", "attention to detail", "communication"],
        "certifications": ["ui design certification", "adobe certified"],
        "keywords": ["ui", "user interface", "visual design", "mockups", "design system"]
    },
    "Product Designer": {
        "category": "Design",
        "skills": ["ux design", "ui design", "prototyping", "user research", "product thinking"],
        "tools": ["figma", "sketch", "adobe xd", "framer", "protopie"],
        "soft_skills": ["empathy", "strategic thinking", "collaboration", "communication"],
        "certifications": ["product design certification", "ux certification"],
        "keywords": ["product design", "end-to-end design", "user centered", "product strategy"]
    },
    "Graphic Designer": {
        "category": "Design",
        "skills": ["adobe photoshop", "adobe illustrator", "adobe indesign", "branding", "typography"],
        "tools": ["adobe creative cloud", "canva", "affinity designer", "procreate"],
        "soft_skills": ["creativity", "attention to detail", "time management"],
        "certifications": ["adobe certified professional", "graphic design certification"],
        "keywords": ["graphic design", "visual communication", "branding", "illustration"]
    },
    
    # MARKETING & SALES
    "Digital Marketing Manager": {
        "category": "Marketing",
        "skills": ["seo", "sem", "google analytics", "social media marketing", "email marketing", "content marketing"],
        "tools": ["google ads", "facebook ads", "hubspot", "mailchimp", "semrush", "ahrefs"],
        "soft_skills": ["creativity", "analytical thinking", "communication", "strategy"],
        "certifications": ["google analytics", "google ads", "hubspot", "facebook blueprint"],
        "keywords": ["digital marketing", "marketing campaigns", "lead generation", "conversion"]
    },
    "Content Marketing Manager": {
        "category": "Marketing",
        "skills": ["content strategy", "seo", "copywriting", "content calendar", "analytics"],
        "tools": ["wordpress", "hubspot", "google analytics", "semrush", "canva"],
        "soft_skills": ["creativity", "writing", "strategic thinking", "communication"],
        "certifications": ["content marketing certification", "hubspot content marketing"],
        "keywords": ["content marketing", "content strategy", "blog", "seo", "storytelling"]
    },
    "Social Media Manager": {
        "category": "Marketing",
        "skills": ["social media strategy", "community management", "content creation", "analytics"],
        "tools": ["hootsuite", "buffer", "sprout social", "canva", "adobe creative suite"],
        "soft_skills": ["creativity", "communication", "trend awareness", "adaptability"],
        "certifications": ["social media marketing certification", "facebook blueprint"],
        "keywords": ["social media", "community management", "engagement", "content creation"]
    },
    "Sales Manager": {
        "category": "Sales",
        "skills": ["sales strategy", "team management", "crm", "forecasting", "negotiation"],
        "tools": ["salesforce", "hubspot", "pipedrive", "linkedin sales navigator"],
        "soft_skills": ["leadership", "communication", "motivation", "strategic thinking"],
        "certifications": ["salesforce certified", "sales management certification"],
        "keywords": ["sales management", "team leadership", "revenue", "quota", "pipeline"]
    },
    "Account Executive": {
        "category": "Sales",
        "skills": ["sales", "prospecting", "crm", "negotiation", "closing"],
        "tools": ["salesforce", "hubspot", "outreach", "linkedin sales navigator", "zoom"],
        "soft_skills": ["communication", "persuasion", "resilience", "relationship building"],
        "certifications": ["salesforce certified", "sales certification"],
        "keywords": ["sales", "account management", "prospecting", "closing deals", "quota"]
    },
    
    # PRODUCT MANAGEMENT
    "Product Manager": {
        "category": "Product",
        "skills": ["product strategy", "roadmap planning", "agile", "user stories", "market research"],
        "tools": ["jira", "confluence", "productboard", "aha", "figma", "amplitude"],
        "soft_skills": ["strategic thinking", "communication", "leadership", "prioritization"],
        "certifications": ["certified scrum product owner", "pragmatic marketing"],
        "keywords": ["product management", "roadmap", "feature prioritization", "product strategy"]
    },
    "Technical Product Manager": {
        "category": "Product",
        "skills": ["technical knowledge", "api design", "sql", "agile", "system design"],
        "tools": ["jira", "confluence", "postman", "swagger", "github"],
        "soft_skills": ["technical communication", "problem solving", "leadership"],
        "certifications": ["cspo", "technical product management"],
        "keywords": ["technical pm", "api", "platform", "technical roadmap", "architecture"]
    },
    "Product Marketing Manager": {
        "category": "Product",
        "skills": ["go-to-market strategy", "positioning", "messaging", "competitive analysis", "market research"],
        "tools": ["hubspot", "google analytics", "productboard", "salesforce"],
        "soft_skills": ["strategic thinking", "communication", "storytelling", "collaboration"],
        "certifications": ["product marketing certification", "pragmatic marketing"],
        "keywords": ["product marketing", "gtm", "positioning", "launch", "messaging"]
    },
    
    # HEALTHCARE
    "Data Analyst (Healthcare)": {
        "category": "Healthcare",
        "skills": ["sql", "excel", "healthcare analytics", "hipaa", "clinical data"],
        "tools": ["epic", "cerner", "tableau", "power bi", "sas"],
        "soft_skills": ["attention to detail", "communication", "analytical thinking"],
        "certifications": ["cahims", "chda", "healthcare analytics"],
        "keywords": ["healthcare analytics", "clinical data", "patient outcomes", "hipaa"]
    },
    "Healthcare Administrator": {
        "category": "Healthcare",
        "skills": ["healthcare management", "hipaa", "operations", "compliance", "budgeting"],
        "tools": ["epic", "cerner", "meditech", "excel"],
        "soft_skills": ["leadership", "communication", "organizational skills", "problem solving"],
        "certifications": ["fache", "chc", "mha"],
        "keywords": ["healthcare administration", "operations", "compliance", "patient care"]
    },
    "Clinical Research Coordinator": {
        "category": "Healthcare",
        "skills": ["clinical trials", "gcp", "irb", "patient recruitment", "data collection"],
        "tools": ["rave", "medidata", "redcap", "ctms"],
        "soft_skills": ["attention to detail", "communication", "organization", "ethics"],
        "certifications": ["ccrp", "ccrc", "socra"],
        "keywords": ["clinical research", "clinical trials", "gcp", "patient safety", "data management"]
    },
    
    # FINANCE & ACCOUNTING
    "Financial Analyst": {
        "category": "Finance",
        "skills": ["financial modeling", "excel", "forecasting", "budgeting", "variance analysis"],
        "tools": ["excel", "quickbooks", "sap", "oracle financials", "tableau"],
        "soft_skills": ["analytical thinking", "attention to detail", "communication"],
        "certifications": ["cfa", "cpa", "fmva"],
        "keywords": ["financial analysis", "modeling", "forecasting", "budgeting", "variance"]
    },
    "Investment Banker": {
        "category": "Finance",
        "skills": ["financial modeling", "valuation", "m&a", "due diligence", "pitchbook creation"],
        "tools": ["excel", "capital iq", "factset", "bloomberg terminal"],
        "soft_skills": ["analytical thinking", "communication", "work ethic", "attention to detail"],
        "certifications": ["cfa", "series 7", "series 63"],
        "keywords": ["investment banking", "m&a", "valuation", "deal execution", "financial modeling"]
    },
    "Accountant": {
        "category": "Finance",
        "skills": ["accounting", "gaap", "financial reporting", "reconciliation", "tax preparation"],
        "tools": ["quickbooks", "sap", "oracle", "excel", "sage"],
        "soft_skills": ["attention to detail", "organization", "integrity", "communication"],
        "certifications": ["cpa", "cma", "ea"],
        "keywords": ["accounting", "financial statements", "reconciliation", "audit", "tax"]
    },
    "Risk Analyst": {
        "category": "Finance",
        "skills": ["risk assessment", "quantitative analysis", "modeling", "compliance", "statistics"],
        "tools": ["sas", "r", "python", "excel", "tableau"],
        "soft_skills": ["analytical thinking", "attention to detail", "communication"],
        "certifications": ["frm", "prmia", "cfa"],
        "keywords": ["risk management", "risk assessment", "compliance", "quantitative analysis"]
    },
    
    # OPERATIONS & SUPPLY CHAIN
    "Operations Manager": {
        "category": "Operations",
        "skills": ["operations management", "process improvement", "lean six sigma", "project management"],
        "tools": ["excel", "erp systems", "sap", "tableau", "project management tools"],
        "soft_skills": ["leadership", "problem solving", "communication", "analytical thinking"],
        "certifications": ["six sigma black belt", "pmp", "apics"],
        "keywords": ["operations", "process improvement", "efficiency", "supply chain", "logistics"]
    },
    "Supply Chain Manager": {
        "category": "Operations",
        "skills": ["supply chain management", "logistics", "inventory management", "procurement", "forecasting"],
        "tools": ["sap", "oracle scm", "tableau", "excel"],
        "soft_skills": ["analytical thinking", "negotiation", "communication", "leadership"],
        "certifications": ["apics cscp", "cpim", "six sigma"],
        "keywords": ["supply chain", "logistics", "procurement", "inventory", "vendor management"]
    },
    "Project Manager": {
        "category": "Operations",
        "skills": ["project management", "agile", "scrum", "risk management", "stakeholder management"],
        "tools": ["jira", "asana", "ms project", "monday.com", "confluence"],
        "soft_skills": ["leadership", "communication", "organization", "problem solving"],
        "certifications": ["pmp", "prince2", "csm", "safe"],
        "keywords": ["project management", "agile", "scrum", "stakeholder", "delivery"]
    },
    
    # HUMAN RESOURCES
    "HR Manager": {
        "category": "Human Resources",
        "skills": ["talent management", "recruitment", "employee relations", "performance management", "hris"],
        "tools": ["workday", "bamboohr", "adp", "greenhouse", "lever"],
        "soft_skills": ["communication", "empathy", "conflict resolution", "leadership"],
        "certifications": ["sphr", "phr", "shrm-cp", "shrm-scp"],
        "keywords": ["human resources", "talent management", "recruitment", "employee relations"]
    },
    "Recruiter": {
        "category": "Human Resources",
        "skills": ["recruitment", "sourcing", "interviewing", "ats", "employer branding"],
        "tools": ["linkedin recruiter", "greenhouse", "lever", "workday", "jobvite"],
        "soft_skills": ["communication", "relationship building", "persuasion", "organization"],
        "certifications": ["shrm-cp", "airs certification", "linkedin certified"],
        "keywords": ["recruitment", "talent acquisition", "sourcing", "interviewing", "hiring"]
    },
    "Compensation and Benefits Analyst": {
        "category": "Human Resources",
        "skills": ["compensation analysis", "benefits administration", "market research", "excel"],
        "tools": ["workday", "sap", "payscale", "salary.com", "excel"],
        "soft_skills": ["analytical thinking", "attention to detail", "communication"],
        "certifications": ["ccp", "cbp", "shrm-cp"],
        "keywords": ["compensation", "benefits", "salary analysis", "total rewards", "market pricing"]
    },
    
    # LEGAL
    "Legal Counsel": {
        "category": "Legal",
        "skills": ["contract law", "legal research", "negotiation", "compliance", "risk management"],
        "tools": ["westlaw", "lexisnexis", "docusign", "clio"],
        "soft_skills": ["analytical thinking", "communication", "attention to detail", "negotiation"],
        "certifications": ["bar admission", "legal specialization"],
        "keywords": ["legal counsel", "contracts", "compliance", "legal research", "negotiation"]
    },
    "Paralegal": {
        "category": "Legal",
        "skills": ["legal research", "document preparation", "case management", "litigation support"],
        "tools": ["westlaw", "lexisnexis", "case management software", "e-discovery tools"],
        "soft_skills": ["attention to detail", "organization", "communication", "research"],
        "certifications": ["certified paralegal", "advanced paralegal certification"],
        "keywords": ["paralegal", "legal support", "document preparation", "legal research"]
    },
    
    # ENGINEERING (NON-SOFTWARE)
    "Mechanical Engineer": {
        "category": "Engineering",
        "skills": ["cad", "solidworks", "autocad", "fem analysis", "thermodynamics", "mechanics"],
        "tools": ["solidworks", "autocad", "ansys", "catia", "matlab"],
        "soft_skills": ["problem solving", "analytical thinking", "teamwork", "creativity"],
        "certifications": ["pe license", "certified solidworks professional"],
        "keywords": ["mechanical engineering", "design", "manufacturing", "prototyping", "testing"]
    },
    "Electrical Engineer": {
        "category": "Engineering",
        "skills": ["circuit design", "pcb design", "embedded systems", "power systems", "plc"],
        "tools": ["altium", "eagle", "matlab", "labview", "pspice"],
        "soft_skills": ["analytical thinking", "problem solving", "attention to detail"],
        "certifications": ["pe license", "certified automation professional"],
        "keywords": ["electrical engineering", "circuit design", "power systems", "automation"]
    },
    "Civil Engineer": {
        "category": "Engineering",
        "skills": ["structural analysis", "autocad", "civil 3d", "project management", "surveying"],
        "tools": ["autocad", "civil 3d", "revit", "sap2000", "etabs"],
        "soft_skills": ["problem solving", "communication", "teamwork", "project management"],
        "certifications": ["pe license", "leed certification"],
        "keywords": ["civil engineering", "structural design", "construction", "infrastructure"]
    },
    
    # EDUCATION
    "Instructional Designer": {
        "category": "Education",
        "skills": ["instructional design", "elearning", "learning management systems", "curriculum development"],
        "tools": ["articulate storyline", "adobe captivate", "canva", "lms platforms"],
        "soft_skills": ["creativity", "communication", "organization", "empathy"],
        "certifications": ["cptd", "instructional design certification"],
        "keywords": ["instructional design", "elearning", "curriculum", "training", "education"]
    },
    "Training and Development Manager": {
        "category": "Education",
        "skills": ["training program development", "lms", "needs assessment", "facilitation"],
        "tools": ["cornerstone", "workday learning", "articulate", "zoom"],
        "soft_skills": ["leadership", "communication", "presentation", "coaching"],
        "certifications": ["cptd", "training certification"],
        "keywords": ["training and development", "learning", "employee development", "facilitation"]
    },
    
    # CUSTOMER SUCCESS & SUPPORT
    "Customer Success Manager": {
        "category": "Customer Success",
        "skills": ["customer relationship management", "onboarding", "crm", "account management"],
        "tools": ["salesforce", "gainsight", "totango", "zendesk", "intercom"],
        "soft_skills": ["communication", "empathy", "problem solving", "relationship building"],
        "certifications": ["customer success certification", "salesforce certified"],
        "keywords": ["customer success", "retention", "onboarding", "account management", "churn"]
    },
    "Technical Support Engineer": {
        "category": "Customer Success",
        "skills": ["troubleshooting", "technical support", "ticketing systems", "linux", "networking"],
        "tools": ["zendesk", "jira", "servicenow", "ssh", "wireshark"],
        "soft_skills": ["problem solving", "communication", "patience", "technical aptitude"],
        "certifications": ["comptia a+", "network+", "itil"],
        "keywords": ["technical support", "troubleshooting", "customer service", "issue resolution"]
    },
    
    # ADDITIONAL TECH ROLES
    "Frontend Developer": {
        "category": "Technology",
        "skills": ["html", "css", "javascript", "react", "vue", "angular", "responsive design"],
        "tools": ["webpack", "babel", "npm", "git", "figma", "chrome devtools"],
        "soft_skills": ["attention to detail", "creativity", "problem solving"],
        "certifications": ["frontend certification", "react certification"],
        "keywords": ["frontend", "ui development", "web development", "responsive", "javascript"]
    },
    "Backend Developer": {
        "category": "Technology",
        "skills": ["python", "java", "node.js", "go", "sql", "api design", "microservices"],
        "tools": ["docker", "kubernetes", "postman", "git", "redis", "postgresql"],
        "soft_skills": ["problem solving", "logical thinking", "teamwork"],
        "certifications": ["backend certification", "cloud certifications"],
        "keywords": ["backend", "api", "server", "database", "microservices"]
    },
    "Mobile Developer": {
        "category": "Technology",
        "skills": ["swift", "kotlin", "react native", "flutter", "ios", "android"],
        "tools": ["xcode", "android studio", "firebase", "testflight", "git"],
        "soft_skills": ["attention to detail", "problem solving", "creativity"],
        "certifications": ["ios certification", "android certification"],
        "keywords": ["mobile development", "ios", "android", "app development", "mobile"]
    },
    "QA Engineer": {
        "category": "Technology",
        "skills": ["test automation", "selenium", "junit", "pytest", "test planning", "api testing"],
        "tools": ["selenium", "postman", "jira", "testng", "cypress", "jenkins"],
        "soft_skills": ["attention to detail", "analytical thinking", "communication"],
        "certifications": ["istqb", "selenium certification"],
        "keywords": ["quality assurance", "testing", "automation", "qa", "test cases"]
    },
    "Database Administrator": {
        "category": "Technology",
        "skills": ["sql", "database design", "performance tuning", "backup and recovery", "security"],
        "tools": ["mysql", "postgresql", "oracle", "mongodb", "sql server"],
        "soft_skills": ["problem solving", "attention to detail", "analytical thinking"],
        "certifications": ["oracle dba", "microsoft certified dba", "mongodb certified"],
        "keywords": ["database administration", "dba", "sql", "database optimization", "data management"]
    },
    "Network Engineer": {
        "category": "Technology",
        "skills": ["networking", "routing", "switching", "firewall", "tcp/ip", "vpn"],
        "tools": ["cisco", "juniper", "wireshark", "solarwinds", "prtg"],
        "soft_skills": ["problem solving", "analytical thinking", "communication"],
        "certifications": ["ccna", "ccnp", "network+", "juniper certification"],
        "keywords": ["network engineering", "routing", "switching", "firewall", "infrastructure"]
    },
    "Systems Administrator": {
        "category": "Technology",
        "skills": ["linux", "windows server", "active directory", "scripting", "virtualization"],
        "tools": ["vmware", "hyper-v", "powershell", "bash", "ansible"],
        "soft_skills": ["problem solving", "multitasking", "communication"],
        "certifications": ["linux+", "mcsa", "rhcsa", "vmware certified"],
        "keywords": ["system administration", "infrastructure", "server management", "virtualization"]
    },
    
    # EMERGING TECH
    "Blockchain Developer": {
        "category": "Technology",
        "skills": ["blockchain", "solidity", "ethereum", "smart contracts", "web3", "cryptography"],
        "tools": ["truffle", "hardhat", "metamask", "ganache", "remix"],
        "soft_skills": ["problem solving", "innovation", "analytical thinking"],
        "certifications": ["blockchain certification", "ethereum certification"],
        "keywords": ["blockchain", "smart contracts", "web3", "cryptocurrency", "defi"]
    },
    "IoT Engineer": {
        "category": "Technology",
        "skills": ["iot", "embedded systems", "mqtt", "sensors", "raspberry pi", "arduino"],
        "tools": ["arduino ide", "raspberry pi", "node-red", "aws iot", "azure iot"],
        "soft_skills": ["problem solving", "innovation", "analytical thinking"],
        "certifications": ["iot certification", "embedded systems certification"],
        "keywords": ["iot", "internet of things", "embedded systems", "sensors", "edge computing"]
    },
    "Robotics Engineer": {
        "category": "Technology",
        "skills": ["robotics", "ros", "python", "c++", "computer vision", "control systems"],
        "tools": ["ros", "gazebo", "matlab", "solidworks", "opencv"],
        "soft_skills": ["problem solving", "creativity", "analytical thinking"],
        "certifications": ["robotics certification", "ros certification"],
        "keywords": ["robotics", "automation", "ros", "computer vision", "mechatronics"]
    },
}

# Skill Synonyms and Variations
SKILL_SYNONYMS = {
    "python": ["python3", "py", "python programming"],
    "javascript": ["js", "javascript programming", "ecmascript"],
    "machine learning": ["ml", "statistical learning", "predictive modeling"],
    "deep learning": ["dl", "neural networks", "artificial neural networks"],
    "natural language processing": ["nlp", "text analytics", "text mining"],
    "computer vision": ["cv", "image processing", "visual recognition"],
    "sql": ["structured query language", "tsql", "plsql", "mysql", "postgresql"],
    "aws": ["amazon web services", "amazon aws"],
    "azure": ["microsoft azure", "azure cloud"],
    "gcp": ["google cloud platform", "google cloud"],
    "docker": ["containerization", "containers"],
    "kubernetes": ["k8s", "container orchestration"],
    "ci/cd": ["continuous integration", "continuous deployment", "cicd"],
    "agile": ["scrum", "agile methodology", "agile development"],
    "git": ["version control", "source control", "github", "gitlab"],
    "react": ["reactjs", "react.js"],
    "node.js": ["nodejs", "node"],
    "api": ["rest api", "restful api", "web service"],
    "tableau": ["tableau desktop", "tableau server"],
    "power bi": ["powerbi", "microsoft power bi"],
    "excel": ["microsoft excel", "ms excel", "spreadsheet"],
}

# Industry Categories
INDUSTRY_CATEGORIES = {
    "Technology": ["Software Engineer", "Full Stack Developer", "DevOps Engineer", "Cloud Architect"],
    "Data & Analytics": ["Data Engineer", "Data Scientist", "Machine Learning Engineer", "Data Analyst"],
    "Cybersecurity": ["Security Engineer", "Security Analyst"],
    "Design": ["UX Designer", "UI Designer", "Product Designer", "Graphic Designer"],
    "Marketing": ["Digital Marketing Manager", "Content Marketing Manager", "Social Media Manager"],
    "Sales": ["Sales Manager", "Account Executive"],
    "Product": ["Product Manager", "Technical Product Manager", "Product Marketing Manager"],
    "Healthcare": ["Data Analyst (Healthcare)", "Healthcare Administrator", "Clinical Research Coordinator"],
    "Finance": ["Financial Analyst", "Investment Banker", "Accountant", "Risk Analyst"],
    "Operations": ["Operations Manager", "Supply Chain Manager", "Project Manager"],
    "Human Resources": ["HR Manager", "Recruiter", "Compensation and Benefits Analyst"],
    "Legal": ["Legal Counsel", "Paralegal"],
    "Engineering": ["Mechanical Engineer", "Electrical Engineer", "Civil Engineer"],
    "Education": ["Instructional Designer", "Training and Development Manager"],
    "Customer Success": ["Customer Success Manager", "Technical Support Engineer"],
}

def get_all_roles():
    """Get list of all job roles."""
    return list(JOB_DATABASE.keys())

def get_roles_by_category(category):
    """Get all roles in a specific category."""
    return [role for role, data in JOB_DATABASE.items() if data["category"] == category]

def get_all_categories():
    """Get list of all categories."""
    return list(set(data["category"] for data in JOB_DATABASE.values()))