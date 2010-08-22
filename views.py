from django.shortcuts import render_to_response, redirect
from mysite.aniface.models import Anime, P_List, AniPerList
from django.contrib.auth.models import User
from django.http import HttpResponse
import os
import glob

# Class to resolve file transfer issues
class FileIterWrapper(object):
  def __init__(self, flo, chunk_size = 1024**2):
    self.flo = flo
    self.chunk_size = chunk_size

  def next(self):
    data = self.flo.read(self.chunk_size)
    if data:
      return data
    else:
      raise StopIteration

  def __iter__(self):
    return self

# Create your views here.

def index(request):
    anime_list = Anime.objects.all().order_by("-a_name")
    return render_to_response('anindex.html', {'anime_list': anime_list})

def anime(request, ap_slug):
    a = Anime.objects.filter(ap_slug__exact=ap_slug)[0]
    os.chdir(a.location)
    flist = glob.glob('*')
    return render_to_response('anime.html',
                              {'anime': a, 'file_list' : flist})

def pr_list(request):
    u = User.objects.get(pk=1) # should be replaced with auth code...
    pl = P_List.objects.all().filter(person=u)
    return render_to_response('plist.html', {'pl' : pl})

def mark(request, ap_slug):
    val = request.GET['ep']
    u = User.objects.get(pk=1)
    a = Anime.objects.get(ap_slug=ap_slug)

    aplist = AniPerList.objects.all().filter(anime=a, person=u)
    if aplist.count == 0:
        apl = aplist[0]
        apl.curr_episode = int(val)
    else:
        apl = AniPerList(anime=a, person=u, curr_episode=int(val))

    apl.save()
    return redirect('/aniface/anime/' + ap_slug)

def confug(request):
    return HttpResponse("Nothing to see here at the moment.")

def play(request, ap_slug):
    a = Anime.objects.filter(ap_slug__exact=ap_slug)[0]
    val = request.GET['fn']
    return HttpResponse(FileIterWrapper(open(a.location + '/' + val)),
                        mimetype='video/x-msvideo')


