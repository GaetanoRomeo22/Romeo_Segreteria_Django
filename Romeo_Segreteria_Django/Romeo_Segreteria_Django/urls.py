"""
URL configuration for Romeo_Segreteria_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from Romeo_Segreteria.views import login_view, account_view, register_view, forgot_password_view

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('', login_view, name='index'), # Pagina iniziale
    path('login/', login_view, name='login'), # Pagina di login
    path('account/', account_view, name='account'), # Pagina dell'area riservata
    path('registrazione/', register_view, name='registrazione'), # Pagina di registrazione
    path('recupero/', forgot_password_view, name='recupero'), # Pagina di recupero password
]
