from django.urls import path
from twitterclone.authentication import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login/', views.loginview, name='login_view'),
    path('logout/', views.logoutview, name='logout_view'),
    path('createuser/', views.CreateUser.as_view(), name='create_user_view')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
