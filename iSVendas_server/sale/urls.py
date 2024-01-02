
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'produtos2', views.ProductAPIView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('produto', views.ProductView.as_view()),
    path('produtos/', views.ProductList.as_view()),
    path('purchase/', views.PurchaseView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

