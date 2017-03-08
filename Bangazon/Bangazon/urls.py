from django.conf.urls import url, include
from Bangazon_api import views
from rest_framework.routers import DefaultRouter
from django.contrib import admin

# Create a router, using DefaultRouter
# Register each ViewSet with it.
router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'payment_method', views.PaymentTypeViewSet)
router.register(r'product_categories', views.ProductTypeViewSet)
router.register(r'product_orders', views.OrderProductViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

