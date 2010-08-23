from mysite.aniface.models import *
from django.contrib.auth.models import User

# this is a crappy version, but less  computational-intensive than generic placement
def MoveUp(apslug, u_id):
    u = User.objects.get(pk=u_id) # get the user
    a = Anime.objects.get(ap_slug=apslug) # get the anime
    
    the_anime = P_List.objects.get(person=u, anime=a)
    ord = the_anime.ordinal
    
    if ord > 1:
        prev_anime = P_List.objects.get(person=u, ordinal=ord - 1)
        the_anime.ordinal = ord - 1
        prev_anime.ordinal = ord
        the_anime.save()
        prev_anime.save()
    
    