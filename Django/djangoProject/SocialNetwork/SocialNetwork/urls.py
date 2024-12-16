from django.contrib import admin
from django.urls import path
from bookface.views import home, register, users_list, photo_gallery, upload_photo, photo_detail
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('list/', users_list, name='list'),
    path('reg/', register, name='register'),
    path('photos/', photo_gallery, name='photo_gallery'),
    path('photos/upload/', upload_photo, name='upload_photo'),
    path('photos/<int:pk>/', photo_detail, name='photo_detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
