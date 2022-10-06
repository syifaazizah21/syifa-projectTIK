"""untirta URL Configuration

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
from feb.views import Feb
from fh.views import prodifh
from fkip.views import prodifkip
from ft.views import prodift
from pascasarjana.views import prodipasca
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('feb/', Feb, name="feb"),
    path('fh/', prodifh, name="fh"),
    path('fkip/', prodifkip, name="fkip"),
    path('ft/', prodift, name="ft"),
    path('pascasarjana/', prodipasca, name="pascasarjana"),
]
