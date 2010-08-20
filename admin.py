from mysite.aniface.models import PerProfile, Anime, P_List
from django.contrib import admin

#class ProfInline(admin.TabularInline):
#    model = PerProfile

admin.site.register(Anime)
