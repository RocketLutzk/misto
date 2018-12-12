from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('search/', views.Boxview.as_view(), name='list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registration_view, name='signup'),
    path('create/', views.create_box, name='create_box'),
    path('userpost/', views.user_post, name='user_post')
]
