from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Resume

# matching/ai_engine.py

def match_resume_to_job(resume_text, job):
    """
    resume_text: str (text extracted from PDF)
    job: Job object
    """
    if not isinstance(resume_text, str):
        raise ValueError("resume_text must be string")

    # Example simple match score
    job_keywords = job.skills_required.lower().split(",")
    resume_words = resume_text.lower().split()

    matches = sum(1 for kw in job_keywords if kw.strip() in resume_words)
    score = (matches / max(len(job_keywords), 1)) * 100
    return round(score, 2)


def rank_candidates(job):
    resumes = Resume.objects.filter(candidate__role='candidate')

    ranked = []

    for resume in resumes:
        if resume.extracted_text:
            score = match_resume_to_job(resume.extracted_text, job)
            ranked.append((resume.candidate.username, score))

    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked
