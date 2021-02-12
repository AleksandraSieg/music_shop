from django.urls import path
from . import views
from musicapp.settings import DEBUG, STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-cd'),
    path('update/<int:cd_id>', views.update_cd),
    path('delete/<int:cd_id>', views.delete_cd)
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
