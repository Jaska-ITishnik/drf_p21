from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import ProductListCreateAPIView, CategoryListCreateAPIView, RegisterCreateAPIView

urlpatterns = [
    path('products', ProductListCreateAPIView.as_view()),
    path('category', CategoryListCreateAPIView.as_view()),
    path('register', RegisterCreateAPIView.as_view()),
    path('token-auth/', views.obtain_auth_token),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
