from datetime import datetime
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import forms, views


urlpatterns = [
    path('signup/', views.userSignup, name='signup'),
    path('login/', views.userLogin, name='login' ),
    path('logout/', views.userLogout, name='logout'),
    #path('login/',
    #     LoginView.as_view
    #     (
    #         template_name='users/login.html',
    #         authentication_form=forms.loginForm,
    #         extra_context=
    #         {
    #             'title': 'Log in',
    #             'year' : datetime.now().year,
    #         }
    #     ),
    #     name='login'),
    #path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]
