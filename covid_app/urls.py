from django.urls import path
from .views import CovidDetailView,MyRecords
urlpatterns = [
    
    path('',MyRecords.as_view(),name="RECORDS"),
    path('<int:pk>', CovidDetailView.as_view(),name='Details'),
    
   
]