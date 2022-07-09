from django.urls import path
from base import views

urlpatterns=[
    path('',views.index),
    path('create/',views.create),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
]