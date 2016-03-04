from django.conf.urls import *
from calculator import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^submit$', views.submit, name='index'),
	url(r'^view$', views.viewSalary, name='index'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
