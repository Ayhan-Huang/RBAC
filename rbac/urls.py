from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/$', views.users),
    url(r'^users/new/$', views.users_new),
    url(r'^users/edit/(?P<id>\d+)/$', views.users_edit),
    url(r'^users/delete/(?P<id>\d+)/$', views.users_delete),

    url(r'^roles/$', views.roles),
    url(r'^roles/new/$', views.roles_new),
    url(r'^roles/edit/(?P<id>\d+)/$', views.roles_edit),
    url(r'^roles/delete/(?P<id>\d+)/$', views.roles_delete),

    url(r'^permissions/$', views.permissions),
    url(r'^permissions/new/$', views.permissions_new),
    url(r'^permissions/edit/(?P<id>\d+)/$', views.permissions_edit),
    url(r'^permissions/delete/(?P<id>\d+)/$', views.permissions_delete),

    url(r'^menus/$', views.menus),
    url(r'^menus/new/$', views.menus_new),
    url(r'^menus/edit/(?P<id>\d+)/$', views.menus_edit),
    url(r'^menus/delete/(?P<id>\d+)/$', views.menus_delete),

    url(r'^$', views.index)
]
