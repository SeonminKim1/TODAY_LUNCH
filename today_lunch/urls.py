"""join_login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from users import views as userview
from restaurant import views as resview
from mypage import views as mypageview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userview.init_view, name='init'),
    
    # user - join, login, logout
    path('user/join/', userview.join_view, name='join'),
    path('user/login/', userview.login_view, name='login'),
    path('user/logout/', userview.logout, name='logout'),

    # register 2
    path('user/scoring_view/', resview.scoring_view, name='scoring_view'),
    path('user/put_score/', resview.put_score, name='put_score'),

    # main
    path('main/', resview.main_view, name='main'),

    # mypage
    path('mypage/<int:year>/<int:month>', mypageview.mypage_view, name='mypage'),
    path('mypage/diary/create/', mypageview.create_diary, name='create_diary'),
    path('mypage/diary/update/', mypageview.update_diary, name='update_diary'),
    path('mypage/diary/delete/', mypageview.delete_diary, name='delete_diary'),
    path('mypage/', mypageview.redirect_view, name='nav_mypage'),
]