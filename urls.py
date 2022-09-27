from django.urls import path,include
from django.views import View
from .import views

urlpatterns = [
    path('',views.Indexpage,name='indexpage'),
    path('about/',views.aboutus,name='about'),
    
    path('chart_page/',views.charts_page,name='charts_page'),
    path('password_page/',views.password_page,name='password_page'),
    path('teams_page/',views.teams_page,name='teams_page'),
    path('table_page/',views.table_page,name='table_page'),
    path('event_page/',views.event_page,name='event_page'),
    path('layout_1/',views.layout_1,name='layout_1'),
    path('layout_2/',views.layout_2,name='layout_2'),
    path('Not_Found/',views.Not_Found,name='Not_Found'),
    path('admin_reg/',views.admin_reg,name='admin_reg'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('register/',views.ad_register,name='register'),
    path('login/',views.ad_login,name='login'),
    path('ad_index/',views.Admin_index,name='ad_index'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile_update/',views.edit_profile,name='profile_update'),
    path('all_artist/',views.all_artist,name='all_artitst'),
    path('add_artits/', views.add_artits, name='add_artits'),
    path('delete_artist/<int:pk>/',views.Delete_artitst,name='delete_artist'),
    path('register_user/',views.register_user,name='register_user'),
    path('login-user/',views.login_user,name='login-user'),
    path('logout_user/',views.logout_user,name="logout_user"),
    path('feedback/',views.feedback,name='feedback'),
    path('all_feedback/',views.all_feedback,name='all_feedback'),
    path('all_followers/',views.all_followers,name='all_followers'),
    path('book_show/',views.book_show,name='book_show'),
    path('all_show/',views.all_show,name='all_show'),
    path('add_video/',views.add_video,name='add_video'),   
    path('about_band/',views.about_band,name='about_band'),
    path('contact/',views.contact,name='contact'),
    path('test/',views.test,name='test'),
    
]
