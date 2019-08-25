from django.conf.urls import url                                                                                                                              
from . import views
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [ 
    url('', views.default_map, name="default"),
    # url(r'^admin/', include(admin.site.urls)),
]