from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('register/<int:event_id>/', views.register_for_event, name='register_for_event'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
