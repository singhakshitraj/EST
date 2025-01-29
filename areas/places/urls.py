from django.urls import path
from . import views
urlpatterns = [
    path('',view=views.front,name='Front'),
    path('search',view=views.search,name="Search Page"),
    path('property/add/new/',view=views.createProperty,name = 'Create Property'),
    path('property/<str:id>/',view=views.viewProperty,name='Property Details'),
    path('property/<str:id>/purchase/',view=views.purchaseProperty,name='Purchase Property'),
    path('property/<str:id>/confirm/',view=views.confirm,name='Confirm Purchase'),
    path('property/error/invalid_operation/',view=views.invalidOperation,name='Invalid Operation'),
    path('login/',view=views.login_,name='Login-Page'),
    path('register/',view=views.register_,name='Register-Page'),
    path('logout/',view=views.logout_,name = "Logout-Page"),
]
