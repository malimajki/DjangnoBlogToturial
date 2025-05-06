from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import home_view, post_detail_view, post_create_view, post_update_view, post_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", home_view, name='home'),
    path('post/new', post_create_view, name='post_create'),
    path('post/<str:slug>', post_detail_view, name='post_detail'),
    path('post/<str:slug>/edit', post_update_view, name='post_update'),
    path('post/<str:slug>/delete', post_delete_view, name='post_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)