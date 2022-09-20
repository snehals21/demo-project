from django.urls import path, include
from .api import CreateBlogApi, ListBlogApi, UpdateBlogApi, DeleteBlogApi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from .views import hello
urlpatterns = [
    path('api', ListBlogApi.as_view()),
    path('api/create', CreateBlogApi.as_view()),
    path('api/<int:pk>', UpdateBlogApi.as_view()),
    path('api/<int:pk>/delete', DeleteBlogApi.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('test/api', hello)
]
