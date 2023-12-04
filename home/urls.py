from django.urls import path,include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.store, name='store'),
    path('', views.home, name='home'),
    path('email_message/', views.email_message, name='email_message'),
    
]