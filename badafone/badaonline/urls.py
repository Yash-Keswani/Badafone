"""badafone URL Configuration

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
from . import views

"""
path('display/<str:table_name>', views.display_table),
path('all_plans', views.all_plans),
path('edit_plan', views.edit_plan),
path('login', views.login_page),
path('user_statistics', views.user_stats),
"""
urlpatterns = [
	path('top_secret', views.import_users),
	path('login_page', views.login_page),
	path('login', views.login, name='authenticate'),
	path('sales', views.sales, name='sales_home'),
	path('admin', views.admin, name='admin_home'),
	path('customer', views.customer, name='customer_home'),
	path('employee', views.employee, name='employee_home'),
	path('<str:page>', views.wildcard),
]
