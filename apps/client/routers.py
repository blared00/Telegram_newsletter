from rest_framework.routers import DefaultRouter

from apps.client.views import ContactViewSet

router_v1 = DefaultRouter()
router_v1.register(
    'client',
    ContactViewSet,
    basename='client'
)
