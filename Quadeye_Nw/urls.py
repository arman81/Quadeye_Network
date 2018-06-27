from django.conf.urls import include, url
from django.contrib import admin
from locater import views
from django.conf.urls import include
urlpatterns = [
    # Examples:
    # url(r'^$', 'Quadeye_Nw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^locater/',include('locater.urls')),
    url(r'^map',views.marker,name='marker'),
    url(r'^add_dc',views.add_centre,name='add_centre'),
    url(r'^add_link',views.add_link,name='add_link'),
]
