from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def recruiter_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        # Not logged in
        if not request.user.is_authenticated:
            return redirect('login')

        # Candidate trying to access
        if request.user.role == 'candidate':
            return HttpResponseForbidden("You are not authorized to access this page.")

        # Pending recruiter
        if request.user.role == 'pending_recruiter':
            return HttpResponseForbidden("Waiting for admin approval.")

        # Approved recruiter
        if request.user.role == 'recruiter':
            return view_func(request, *args, **kwargs)

        return HttpResponseForbidden("Access Denied.")

    return wrapper