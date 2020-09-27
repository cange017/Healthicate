from django.urls import path
from django.conf.urls import url
from .import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     path('employee_register/',views.employee_register.as_view(), name='employee_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     # url(r'^$', views.all_rooms, name="all_rooms"),
     # url(r'rooms/(?P<slug>[-\w]+)/$', views.room_detail, name="room_detail"),
]