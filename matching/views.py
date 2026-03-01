
	
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from jobs.models import Job, Application
from .models import Resume
from .ai_engine import match_resume_to_job
import PyPDF2


def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


@login_required
def upload_resume(request, job_id):

    if request.user.role != "candidate":
        return redirect('job_list')

    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':

        # Prevent duplicate job application FIRST
        if Application.objects.filter(job=job, candidate=request.user).exists():
            messages.warning(request, "You already applied for this job.")
            return redirect('job_list')

        resume_file = request.FILES.get('resume')

        if not resume_file:
            messages.error(request, "Please upload a resume.")
            return redirect('upload_resume', job_id=job.id)

        # Extract text
        resume_text = extract_text_from_pdf(resume_file)

        # Reset pointer
        resume_file.seek(0)

        # Save resume with extracted text
        resume_instance = Resume.objects.create(
            candidate=request.user,
            job=job,
            resume_file=resume_file,
            extracted_text=resume_text
        )

        # Calculate score
        score = match_resume_to_job(resume_text, job)

        # Create application
        Application.objects.create(
            job=job,
            candidate=request.user,
            match_score=score,
            resume=resume_instance
        )

        messages.success(request, "Application submitted successfully!")
        return redirect('job_list')

    return render(request, 'matching/upload_resume.html', {'job': job})