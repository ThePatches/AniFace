from django.shortcuts import render_to_response, redirect
from mysite.aniface.models import Anime, P_List, AniPerList
from mysite.aniface.mvmt import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseBadRequest
import mysite.aniface.mvmt
import os
import glob


# Create your views here.

def index(request):
    anime_list = Anime.objects.all().order_by("a_name")
    return render_to_response('anindex.html', {'anime_list': anime_list})

def anime(request, ap_slug):
    a = Anime.objects.filter(ap_slug__exact=ap_slug)[0]
    os.chdir(a.location)
    flist = glob.glob('*.txt')
    if request.user.is_authenticated():
        mark = AniPerList.objects.all().filter(person=request.user,
                                                       anime=a)
        if len(mark) == 0:
            marker = 0
        else:
            marker = mark[0].curr_episode
    else:
        marker = 0
    return render_to_response('anime.html',
                              {'anime': a, 'file_list' : flist,
                              'marker' : marker})

@login_required()
def pr_list(request):
    u = request.user
    pl = P_List.objects.all().filter(person=u).order_by('ordinal')
    return render_to_response('plist.html', {'pl' : pl})

@login_required()
def mark(request, ap_slug):
    val = request.GET['ep']
    u = request.user
    a = Anime.objects.get(ap_slug=ap_slug)

    aplist = AniPerList.objects.all().filter(anime=a, person=u)
    if len(aplist) == 0:
        apl = AniPerList(anime=a, person=u, curr_episode=int(val))
    else:
        apl = aplist[0]
        apl.curr_episode = int(val)

    apl.save()
    return redirect('/aniface/anime/' + ap_slug)

def confug(request):
    return HttpResponse("Nothing to see here at the moment.")

@login_required()
def movepl(request, ap_slug):
    val = int(request.GET['dr'])
    u = request.user
    
    if val > 2:
       raise Http404
    
    if val == 1:
        MoveUp(ap_slug, u)
    else:
        MoveDown(ap_slug, u)

    return redirect('/aniface/plist/')
    
@login_required()
def rm_plist(request):
    loc = int(request.GET['loc'])
    u = request.user
    
    if RemFrom(u, loc) == 1:
        return HttpResponseBadRequest('Errors occurred on removal')
    else:
        return redirect('/aniface/plist')
