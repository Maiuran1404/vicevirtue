from django.urls import path

from . import views

urlpatterns = [
    path('all_posts', views.posts, name='all_posts'),
    path('write_post', views.writePost, name='write_post'),
    path('daily_posts', views.dailyPosts, name='daily_posts'),
    #path('set_timezone', views.set_timezone, name='set_timezone'),
    path('select_post', views.selectPost, name='select_post'),
    path('logout', views.logout, name='logout')
]
