from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import TemplateView, View
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView,
    PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView
)

from accounts.forms import (
    RegisterFormView, EditProfileFormView,EditUserInfoFormView,
)

class LogInView(LoginView):
    template_name = 'accounts/login.html'

class LogOutView(LogoutView):
    template_name = 'accounts/logout.html'

class RegsiterView(View):
    template_name = 'accounts/register.html'
    
    def get(self, request):
        form = RegisterFormView()
        context = {
            'form': form,    
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterFormView(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blog:dashboard')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class EditProfileView(View):
    template_name = 'accounts/edit_profile.html'

    def get(self, request):
        form = EditProfileFormView()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = EditProfileFormView(request.POST, instance = request.user)

        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            return redirect('blog:dashboard')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
    

class EditUserInfoView(View):
    template_name = 'accounts/edit_user_info.html'

    def get(self, request):
        form = EditUserInfoFormView()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        profile = request.user.userprofile
        form = EditUserInfoFormView(request.POST, instance = profile)

        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            return redirect('blog:dashboard')
        context = {
            'form':form,
        }
        return render(request, self.template_name, context)


class ChangePasswordView(View, PasswordChangeForm):
    template_name = 'accounts/change_password.html'

    def get(self, request):
        form = PasswordChangeForm(data = request.GET, user = request.user)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


    def post(self, request):
        form = PasswordChangeForm(data = request.POST, user = request.user)

        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            update_session_auth_hash(request, form.user)
            return redirect('blog:dashboard')
        context = {
            'form':form,
        }
        return render(request, self.template_name, context)


class ResetPasswordView(PasswordResetView):
    pass

class ResetPasswordDoneView(PasswordResetDoneView):
    pass

class ResetPasswordConfirmView(PasswordResetConfirmView):
    pass
    
class ResetPasswordComplete(PasswordResetCompleteView):
    pass