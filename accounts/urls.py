from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # accounts/signup
    path('signup/', views.signup, name='signup'),

    # accounts/insert_payment_info
    path('<int:accounts_pk>/modify_user_info', views.modify_user_info, name='modify_user_info'),

    # accounts/login
    path('login/', views.login, name='login'),

    # accounts/logout
    path('logout/', views.logout, name='logout'),
]




