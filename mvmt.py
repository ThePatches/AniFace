from mysite.aniface.models import *
from django.contrib.auth.models import User

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
    
    