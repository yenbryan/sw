from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'fundy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^company/', include('company.urls')),
    url(r'^registration/', include('registration.urls')),

    url(r'^profile/$', 'registration.views.view_profiles', name='view_profiles'),
    url(r'^profile/(?P<username>\w.+)$', 'registration.views.view_profile', name='view_profile'),
    url(r'^follow/profile/(?P<follow>\w.+)$', 'registration.views.follow', name='follow'),

    url(r'^company/$', 'company.views.view_companys', name='view_companys'),
    url(r'^company/(?P<slug>\w+)$', 'company.views.view_company', name='view_company'),

    url(r'^my-profile/$', 'registration.views.my_profile', name='my_profile'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'registration.views.splash_index', name='splash_index'),

]
