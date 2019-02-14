from django.db import models 

#this model represents a single participant in the database
class Participant(models.Model):
    #the participant's name   
    name = models.CharField(max_length = 255) 

    #the paricipant's review status
    status = models.IntegerField(default = 0)

    #the partipant's age
    age = models.IntegerField()

    #whether the partipant has siblings
    siblings = models.BooleanField()

    #list of enviromental exposure of the participant
    exposures = models.TextField()

    #list of participant's known genetic mutations 
    mutations = models.TextField()

