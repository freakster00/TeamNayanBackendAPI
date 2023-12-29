
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from galliMaps.views import Gallimap
from objDetect.views import ImageDetect

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('peopleCount',ImageDetect.as_view()),
    path('gallimaps/navigation',Gallimap.as_view())
    
]
