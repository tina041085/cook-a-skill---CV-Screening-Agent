# CV Screening Agent – System Specification

## 1. Overview

CV Screening Agent is an AI-powered recruitment assistant designed to:

- Parse CV documents (PDF/DOCX)
- Extract structured candidate information
- Compare CV against Job Description (JD)
- Provide ranking and recommendation
This system is designed for scalability from MVP to enterprise-grade HR automation.
---
## 2. System Architecture

### High-Level Flow

CV Upload → Text Extraction → Information Extraction → Embedding → Scoring → Ranking → Output

### Core Components

1. CV Parser
2. JD Parser
3. Skill Extractor
4. Embedding Engine
5. Matching & Scoring Engine
6. Recommendation Engine
7. API Layer (FastAPI)

---

## 3. Functional Requirements

### 3.1 CV Parsing

- Support PDF
- Support DOCX
- Extract raw text
- Normalize formatting

### 3.2 Information Extraction

Extract structured fields:

- Name
- Email
- Skills
- Years of experience
- Education
- Previous companies
- Certifications

Output format:

```json
{
  "skills": [],
  "years_experience": 0,
  "education": "",
  "companies": []
}
3.3 Matching Logic
Level 1 – Keyword Matching
•	Overlapping skills ratio
Level 2 – Semantic Similarity
•	Sentence embedding
•	Cosine similarity
Level 3 – Weighted Scoring
Example:
Final Score =
(0.5 × Semantic Similarity) +
(0.3 × Skill Match Score) +
(0.2 × Experience Score)
________________________________________
3.4 Output Format
{
  "match_score": 0.84,
  "matched_skills": [],
  "missing_skills": [],
  "experience_gap": 1,
  "recommendation": "Strong Candidate"
}
4. Non-Functional Requirements
•	Response time < 2s per CV
•	Modular architecture
•	Easily extendable
•	Production-ready API
________________________________________
5. Future Enhancements
•	Bias detection module
•	Candidate clustering
•	Interview question generation
•	Retention prediction model
•	Dashboard for HR
________________________________________
6. Tech Stack
Backend:
•	Python
•	FastAPI
AI:
•	Sentence Transformers
•	Scikit-learn
Database:
•	PostgreSQL
Optional:
•	LangGraph (Agent Orchestration)
•	Redis (Caching)
________________________________________
7. Roadmap
Phase 1 – MVP
•	CV parsing
•	Embedding similarity
•	Score output
Phase 2 – Advanced Scoring
•	Structured extraction
•	Weighted scoring
•	Skill gap analysis
Phase 3 – AI Agent
•	Multi-step reasoning
•	Explainable decisions
•	Interview assistant
________________________________________
8. Target Use Cases
•	HR internal screening
•	Recruitment agency automation
•	AI-powered hiring SaaS
•	Resume ranking system
________________________________________
9. Success Metrics
•	Precision of shortlist
•	Recall of strong candidates
•	Time saved per hiring cycle
•	HR satisfaction score

