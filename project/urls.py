"""project URL Configuration

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('', views.index),
    path('com_home/', views.com_home),
    path('farmer_reg/', views.farmer_reg),
    path('login/', views.login),
    path('admin_view_far/', views.admin_view_far),
    path('admin_home/', views.admin_home),
    path('farmer_home/', views.farmer_home),
    path('inv_home/', views.inv_home),
    path('user_home/', views.user_home),
    path('user_reg/', views.user_reg),
    path('admin_view_user/', views.admin_view_user),
    path('admin_view_inv/', views.admin_view_inv),
    path('farmer_add_pro/', views.farmer_add_pro),
    path('farmer_view_product/', views.farmer_view_product),
    path('farmer_delete/', views.delete_product),
    path('farmer_update/', views.update_product),
    path('user_view_product/', views.user_view_product),
    path('view_booked_product/', views.user_booked_product),
    path('payment/', views.payment),
    path('farmer_view_booked_product/', views.farmer_view_booked_product),
    path('inv_reg/', views.inv_reg),
    path('farmer_view_inv/', views.farmer_view_inv),
    path('add_scheme/', views.add_scheme),
    path('farmer_view_plan/', views.farmer_view_plan),
    path('farmer_apply_plan/', views.farmer_apply_plan),
    path('calc/', views.calc),
    path('inv_view_loan_req/', views.inv_view_loan_req),
    path('doc/', views.doc),
    path('farmer_view_loan_status/', views.farmer_view_loan_status),
    path('history/', views.history),
    path('add_equipment/', views.add_equipment),
    path('admin_add_seed/', views.admin_add_seed),
    path('admin_add_fert/', views.admin_add_fert),
    path('admin_add_tools/', views.admin_add_tools),
    path('admin_view_pro/', views.admin_view_pro),
    path('admin_delete_product/', views.admin_delete_product),
    path('admin_update_product/', views.admin_update_product),
    path('farmer_view_supply/', views.farmer_view_supply),
    path('farmer_view_seed/', views.farmer_view_seed),
    path('farmer_view_fert/', views.farmer_view_fert),
    path('farmer_view_tools/', views.farmer_view_tools),
    path('farmer_view_cart/', views.farmer_view_cart),
    path('farmer_payment/', views.farmer_payment),
    path('admin_view_booked_sup/', views.admin_view_booked_sup),
]
