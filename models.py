from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Anime(models.Model):
    a_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    ap_slug = models.CharField(max_length=200)
    def __unicode__(self):
        return self.a_name
        

class P_List(models.Model):
    anime = models.ForeignKey(Anime)
    ordinal = models.IntegerField()
    person = models.ForeignKey(User)
    def __unicode__(self):
        return str(self.ordinal) + ", " + self.anime.a_name + ", " + self.person.username
    
class PerProfile(models.Model):
    ap_name = models.CharField(max_length=200)
    ap_pass = models.CharField(max_length=200)
    user = models.ForeignKey(User, unique=True)
    def __unicode__(self):
        return self.user.username

User.profile = property(lambda u: PerProfile.objects.get_or_create(user=u)[0])

class AniPerList(models.Model):
    anime = models.ForeignKey(Anime)
    person = models.ForeignKey(User)
    curr_episode = models.IntegerField()
    def __unicode__(self):
        return self.person.username + ", " + self.anime.a_name
