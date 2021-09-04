from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import galleryView, imageDetailsView, image_location

urlpatterns=[
    path('gallery', galleryView.as_view(), name = 'gallery'),
    # path('gallerydetails/<int:pk>', imageDetailsView.as_view(), name ='imageDetails'),
    re_path(r'^$', views.home, name='home'),
    # re_path(r'gallery', views.gallery, name='gallery'),
    re_path(r'location/(?P<location_name>\w+)/', views.image_location, name='location'),
    re_path(r'category/(?P<category>\w+)/', views.image_category, name='category'),
    re_path(r'^search/', views.search_results, name='search_results'),

    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


