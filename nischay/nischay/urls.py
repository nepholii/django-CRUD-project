"""
URL configuration for nischay project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home.views import *
from veggi.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",home,name="home"),
    path("recepies/",recipies,name="recepies"),
    path("delete-recipie/<id>/",delete_recipie,name="delete_recipie"),
    path("update-recipie/<id>/",update_recipie,name="update_recepie"),
    path("contact/",contact,name="contact"),
    path("about-us/",about,name="about"),
    path("login/",login_page,name="login_page"),
    path("logout/",log_out,name="log_out"),
    path("register/",register_page,name="register_page"),
    path("add-recepies/",add_recepies,name="add_recepies"),
    path("edit-recepies/",edit_recepies,name="add_recepies"),

    path("sucess-page/",sucess_page,name="sucess"),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

