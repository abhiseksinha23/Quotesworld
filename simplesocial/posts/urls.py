from django.urls import path,re_path

from . import views

app_name='posts'

urlpatterns = [
    path("", views.PostList.as_view(), name="all"),
    path("new/", views.CreatePost.as_view(), name="create"),
    re_path(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    re_path(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="single"),
    re_path(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
      re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
      re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]
