from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('exams', views.ExamsView)
router.register('users', views.UsersView)

urlpatterns = [
    path('', include(router.urls))

]
