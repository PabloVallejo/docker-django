from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import HomeView

urlpatterns = [
    url(
        r'',
        HomeView.as_view(),
        name='home',
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
