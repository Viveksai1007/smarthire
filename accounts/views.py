from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import RegisterForm
from .models import User


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            if user.role == 'recruiter':
                messages.success(request, "Account created. Wait for admin approval.")
            else:
                login(request, user)
                return redirect('/')

            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = form.get_user()

        if user.role == 'recruiter' and not user.is_approved:
            messages.error(self.request, "Your account is pending admin approval.")
            return redirect('login')

        return super().form_valid(form)
    


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('job_list')   # goes to home page