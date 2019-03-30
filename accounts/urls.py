from django.urls import path, re_path

from accounts.views import (
    LogInView, LogInViewWithEmail, LogOutView, RegsiterView,
    EditProfileView, EditUserInfoView, ChangePasswordView,
    ResetPasswordView, ResetPasswordDoneView,
    ResetPasswordConfirmView, ResetPasswordComplete,
)

app_name = 'accounts'
urlpatterns = [
    re_path(r'^login/$', LogInView.as_view(), name = 'login'),
    re_path(r'^login/email$', LogInViewWithEmail.as_view(), name = 'loginWithEmail'),
    re_path(r'^logout/$', LogOutView.as_view(), name = 'logout'),

    re_path(r'^register/$', RegsiterView.as_view(), name = 'register'),
    
    re_path(r'^profile/edit/$', EditProfileView.as_view(), name = 'edit_profile'),
    re_path(r'^profile/edit/user_info/$', EditUserInfoView.as_view(), name = 'edit_user_info'),

    re_path(r'^change-password/$', ChangePasswordView.as_view(), name = 'change_password'),

    re_path(r'^reset-password/$', ResetPasswordView.as_view(), name = 'password_reset'),
    re_path(r'^reset-password/done/$', ResetPasswordDoneView.as_view(), name = 'password_reset_done'),
    re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', ResetPasswordConfirmView.as_view(), name = 'password_reset_confirm'),
    re_path(r'^reset-password/complete/$', ResetPasswordComplete.as_view(), name = 'password_reset_complete'),

]