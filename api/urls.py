from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from api.views import *

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('customers',CustomerViewSetView,basename='customers')


urlpatterns = [
    
    path('token/',ObtainAuthToken.as_view()),
    
]+router.urls