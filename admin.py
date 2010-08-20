from mysite.aniface.models import PerProfile, Anime, P_List
from django.contrib import admin

#class ProfInline(admin.TabularInline):
#    model = PerProfile

admin.site.register(PerProfile)
admin.site.register(Anime)
admin.site.register(P_List)
