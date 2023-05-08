from django.urls import path
from .views import user_profile
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('profile/', user_profile, name='user_profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)