from django.urls import path
from login_app import views
urlpatterns=[
    path("",views.render_login,name="render_login"),
    path("perform_login",views.perform_login,name="perform_login"),
    path("perform_logout",views.perform_logout,name="perform_logout"),
    path("admine_dashboard",views.admine_dashboard,name="admine_dashboard"),

]   
