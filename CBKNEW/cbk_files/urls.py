from django.urls import path
from .views import upload_file, banque_misr_upload

urlpatterns = [
    path('', upload_file, name='upload_file'),
    path('upload/', upload_file, name='upload_file'),
    path('banque-misr-upload/', banque_misr_upload, name='banque_misr_upload')
]
