


from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
     path('',views.admins,name='admins'),
        path('admin_log',views.admin_log,name='admin_log'),
        path('admin_login',views.admin_login,name='admin_login'),
        path('admin_logout',views.admin_logout,name='admin_logout'),
        path('admin_ins',views.admin_ins,name='admin_ins'),
        path('admin_insert',views.admin_insert,name='admin_insert'),
        path('admin_edit/<int:id>',views.admin_edit,name='admin_edit'),
        path('admin_update/<int:id>',views.admin_update,name='admin_update'),
        path('admin_delete/<int:id>',views.admin_delete,name='admin_delete')


]