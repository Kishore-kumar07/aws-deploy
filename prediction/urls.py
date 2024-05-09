from django.contrib import admin
from django.urls import path
from .views import index,predict_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('predict/',predict_view)

]