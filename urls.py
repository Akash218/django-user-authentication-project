from django.urls import path
from .import views
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView

urlpatterns = [
    path('register/', views.register, name="register"),
    path('',views.loginpage,name="login"),
    path('logout/',views.logoutuser),
    path('view/',views.view),
    path('update/',views.Editprofile),
    path('accounts/profile/',views.profile),
    path('password_reset/',PasswordResetView.as_view(),name="reset_password"),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_sent/',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
