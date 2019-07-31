"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import first.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', first.views.layout, name='layout'),
    path('', first.views.home, name='home'),
    path('first/create/', first.views.create, name='create'),
    path('first/new/', first.views.blogform, name='new'),
    path('first/eat/', first.views.eat, name='eat'),
    path('first/<int:pk>/edit/', first.views.edit, name='edit'),
    path('first/<int:pk>/remove/', first.views.remove, name='remove'),
    path('first/detail/<int:blog_id>/', first.views.detail, name='detail'),
    path('first/comment_edit/<int:blog_id>/<int:comment_id>/',first.views.comment_edit, name='comment_edit'),
    path('first/comment_remove/<int:blog_id>/<int:comment_id>/',first.views.comment_remove, name='comment_remove'),
]
