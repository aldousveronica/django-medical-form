from django.conf.urls import url 
from . import views 

urlpatterns = [ 
    #url for participant entry main page
    url('^enter/?$', views.enterparticipant, name="enterparticipant"), 
    #url for list of participants 
    url('^list/?$', views.listofparticipants, name="list"),
    #url to delete all participants
    url('^delete/?$', views.delete, name="delete"),
    #url for updating the review status of a participant
    url('^list/status/?$', views.status, name="status")
     ] 
     
     
   