from mysite.aniface.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# this is a crappy version, but less  computational-intensive than generic placement
def MoveUp(apslug, u):
    a = Anime.objects.get(ap_slug=apslug) # get the anime
    
    the_anime = P_List.objects.get(person=u, anime=a)
    ord = the_anime.ordinal
    
    if ord > 1:
        prev_anime = P_List.objects.get(person=u, ordinal=ord - 1)
        the_anime.ordinal = ord - 1
        prev_anime.ordinal = ord
        the_anime.save()
        prev_anime.save()

def MoveDown(apslug, u): #should maybe be user? probably
    a = Anime.objects.get(ap_slug=apslug) # get the anime
    
    the_anime = P_List.objects.get(person=u, anime=a)
    ord = the_anime.ordinal
    
    extra_anime = len(P_List.objects.filter(ordinal__gt=ord))
    if extra_anime > 0:
        next_anime = P_List.objects.get(person=u, ordinal=ord + 1)
        the_anime.ordinal = ord + 1
        next_anime.ordinal = ord
        the_anime.save()
        next_anime.save()

# This will need error handling!    
def PlaceIn(apslug, u, loc):
    a = Anime.objects.get(ap_slug=apslug)
    
    if P_List.objects.filter(anime=a).exists(): # protection against duplicates
        return 1
    
    list_loc = P_List.objects.all().filter(person=u, ordinal=loc)
    if len(list_loc) == 0:
        P_List.objects.create(anime=a, ordinal=loc, person=u)
        return 0
    
    del list_loc
    list_to_change = P_List.objects.all().filter(ordinal__gte=loc)
    
    for entry in list_to_change:
        entry.ordinal = entry.ordinal + 1
        entry.save()
        
    P_List.objects.create(anime=a, ordinal=loc, person=u)
    
    return 0
    
def RemFrom(u, loc):
    
    try:
        to_delete = P_List.objects.get(ordinal=loc)
        to_delete.delete()
        list_to_change = P_List.objects.all().filter(ordinal__gt=loc)
    
        for entry in list_to_change:
            entry.ordinal = entry.ordinal - 1
            entry.save()
            
        return 0
    
    except ObjectDoesNotExist:
        return 1