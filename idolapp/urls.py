from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from idolapp import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idolapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','poll.views.index'),
    url(r'^/','poll.views.index'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^vote/?','poll.views.vote'),
    url(r'^authenticate','poll.views.authentication')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
