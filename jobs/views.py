from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import JobForm
from .models import Job, Application

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jobs.models import Job, Application


# 🔹 Create Job (Recruiter Only)
@login_required
def job_create(request):

    if request.user.role != 'recruiter':
        return redirect('job_list')

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            messages.success(request, "Job posted successfully!")
            return redirect('job_list')
    else:
        form = JobForm()

    return render(request, 'jobs/job_create.html', {'form': form})

from matching.models import Resume

def job_list_view(request):
    jobs = Job.objects.all()

    applied_jobs = []

    if request.user.is_authenticated:
        applied_jobs = Application.objects.filter(
            candidate=request.user
        ).values_list('job_id', flat=True)

    return render(request, 'jobs/job_list.html', {
        'jobs': jobs,
        'applied_jobs': applied_jobs
    })


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, Application

@login_required
def job_candidates(request, job_id):

    if request.user.role != "recruiter":
        return redirect('job_list')

    job = get_object_or_404(Job, id=job_id)

    applications = Application.objects.filter(job=job)\
        .select_related('candidate')\
        .order_by('-match_score')

    return render(request, "jobs/job_candidates.html", {
        "job": job,
        "applications": applications
    })


from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm
from django.contrib.auth.decorators import login_required

