from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path('refresh_token/',TokenRefreshView.as_view()),
    path('verfiy_token/',TokenRefreshView.as_view()),
]
