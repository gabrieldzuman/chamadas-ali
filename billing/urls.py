from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CallRecordViewSet

router = DefaultRouter()
router.register(r'call-records', CallRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
