from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('email/', views.email, name="email"),
    path('blog-list/', views.blogList, name="blog-list"),
    path('blog-details/<str:pk>', views.blogDetails, name="blog-details"),
    path('blog-update/<str:pk>', views.blogUpdate, name="blog-update"),
    path('blog-create/', views.blogCreate, name="blog-create"),
    path('blog-delete/<str:pk>', views.blogDelete, name="blog-delete"),
    # path('^swagger(?P<format>\.json|\.yaml)$',
    #      schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
