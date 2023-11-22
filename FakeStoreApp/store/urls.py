from django.urls import path

from store import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("api/category",views.CategoryView,basename="category")





urlpatterns=[
    
]+router.urls