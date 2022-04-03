from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .import views
#from .views import home,detail,login,register

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    #path('detail',detail,name="detail"),
    path("postComment",views.postComment,name="postComment"),

    path("<slug:purl>/",views.detail,name="detail"),
    path('category/<slug:url>/',views.category,name="category"),
    path("login_data",views.login_data,name='login_data'),
    path("action",views.action,name='action'),
    path("edit",views.edit,name='edit'),
    path("info_update",views.info_update,name='info_update'),
    path('reg',views.reg,name="reg"),
    path('user_login',views.user_login,name="user_login"),
    path('user_log',views.user_log,name="user_log"),
    path('user_register',views.user_register,name="user_register"),
    path('user_reg',views.user_reg,name="user_reg")
]