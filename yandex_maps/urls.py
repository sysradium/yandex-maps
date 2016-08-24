try:
    from django.conf.urls import url, handler500
except ImportError:
    from django.conf.urls.defaults import url, handler500


from .views import yandex_map

urlpatterns = [
    url(r'^map/(?P<map_id>\d+)/$', yandex_map, name='yandex_map'),
]
