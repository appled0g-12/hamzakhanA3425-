"""artist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from artistapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("createsignin",views.createsignin,name="createsignin"),
    path('signin',views.signin,name="signin"),
    path("signout",views.signout,name="signout"), 
    path('createcard/',views.createcard,name='createcard'),
    path('my_card/', views.my_card, name='my_card'),
    path("card_detail/<int:detail_id>/",views.detail_view, name="card_detail"),
    path('card_detail/<int:detail_id>/like_dislike/', views.like_dislike_detail, name='like_dislike_detail'),
    path('card_detail/<int:detail_id>/follow_unfollow/', views.follow_unfollow_detail, name='follow_unfollow_detail'),
    path('card_detail/<int:detail_id>/', views.detail_view, name='detail_view'),
    # path('cardcreate/',views.cardcreate, name="cardcreate"),
    # path('cardcreate/<int:id>/', views.retrieve_card, name='retrieve_card'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
