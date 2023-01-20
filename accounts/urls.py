from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # accounts/signup
    path('signup/', views.signup, name='signup'),

    # accounts/1/2/add_payment_method
    path('<int:accounts_pk>/<int:payment_pk>/add_payment_method/',
    views.add_payment_method,
    name='add_payment_method'
    ),

    # accounts/1/my_page
    path('<int:accounts_pk>/my_page/', views.my_page, name='my_page'),

    # accounts/insert_payment_info
    path('<int:accounts_pk>/modify_user_info', views.modify_user_info, name='modify_user_info'),

    # accounts/login
    path('login/', views.login, name='login'),

    # accounts/logout
    path('logout/', views.logout, name='logout'),
]




