from django.conf.urls import url
from django.contrib import admin
from planner import views

urlpatterns = [
    url(r'^$', views.viewHome, name='home'),
    url(r'^home$', views.viewHome, name='home'),
    url(r'^edit/(?P<taskid>\d+)/?$', views.viewEdit, name='home'),
    url(r'^admin/', admin.site.urls),
]
