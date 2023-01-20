from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # accounts/signup
    path('signup/', views.signup, name='signup'),

    # accounts/insert_payment_info
    path('insert_payment_info', views.insert_payment_info, name='insert_payment_info'),

    # 1/accounts/login
    path('login/', views.login, name='login'),

    # 1/accounts/logout
    path('logout/', views.logout, name='logout'),
]




