from django.urls import path

from accounts.views import (
    LogInView, LogOutView, RegsiterView,
    EditProfileView, EditUserInfoView, ChangePasswordView,
    ResetPasswordView, ResetPasswordDoneView,
    ResetPasswordConfirmView, ResetPasswordComplete,
)

app_name = 'accounts'
urlpatterns = [
    path('login/', LogInView.as_view(), name = 'login'),
    path('logout/', LogOutView.as_view(), name = 'logout'),

    path('register/', RegsiterView.as_view(), name = 'register'),
    
    path('profile/edit/', EditProfileView.as_view(), name = 'edit_profile'),
    path('profile/edit/user_info/', EditUserInfoView.as_view(), name = 'edit_user_info'),

    path('change-password/', ChangePasswordView.as_view(), name = 'change_password'),

    path('reset-password/', ResetPasswordView.as_view(), name = 'password_reset'),
    path('reset-password/done/', ResetPasswordDoneView.as_view(), name = 'password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset-password/complete/', ResetPasswordComplete.as_view(), name = 'password_reset_complete'),

]