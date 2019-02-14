from django.shortcuts import render, redirect
from django.http import HttpResponse 
from myapp.models import Participant

# Create your views here

#method for participant entry main page
def enterparticipant (request):  #1st parameter request 
    context = {} 
    return render(request, 'myapp/form.html', context) #method that generates a String to give back to the user 

#method to delete all participants
def delete (request): # delete database
    Participant.objects.all().delete()
    return redirect("list")

#method for updating the review status of a participant
def status (request):
    p = Participant.objects.filter(id=request.POST["ID"])[0]
    p.status =request.POST["status"] 
    p.save()
    return redirect("list")

#method for list of participants 
def listofparticipants (request):
    if ("participant" in request.POST): # if this is true, then the user came from /enter (and submitted the form)
        p =Participant()  #build participant object, p, and save it in the database 
        p.name = request.POST["participant"]
        p.age = request.POST["age"]
        p.siblings = ("anySiblings" in request.POST)
        p.exposures = request.POST["exposure"]
        p.mutations = request.POST["mutation"]
        p.save() # save to database
    context = { #defining new dictionary
        "allParticipants": Participant.objects.all() # gets all the participants in the database 
    } 

    return render(request, 'myapp/list.html', context)    

    
       