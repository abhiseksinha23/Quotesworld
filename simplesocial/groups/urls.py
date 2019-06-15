from django.urls import path, re_path

from . import views

app_name = 'groups'

urlpatterns = [
    path(r"", views.ListGroups.as_view(), name="all"),
    path(r"new/", views.CreateGroup.as_view(), name="create"),
    re_path(r"^posts/in/(?P<slug>[-\w]+)/$",views.SingleGroup.as_view(),name="single"),
    re_path(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    re_path(r"leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
]
