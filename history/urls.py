from django.urls import path

from history import views

urlpatterns=[
    path("getlistHistorybyuserid/<int:id>",views.getlistHistory,name="getlistHistorybyuserid"),
]