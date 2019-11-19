from django.urls import path
from twitterclone import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('notifications/', views.NotificationView.as_view(),
         name='notificiations_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
