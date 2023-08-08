from django.contrib import admin

# Register your models here.

from . import models

class HabitantAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'nationality',
    'contact')
    
admin.site.register(models.Habitant, HabitantAdmin)
admin.site.register(models.Acteur)
admin.site.register(models.Activity)
admin.site.register(models.CarnetSante)
admin.site.register(models.ReferentielMetier)
admin.site.register(models.Communauty)
admin.site.register(models.joboffer)
admin.site.register(models.Postulation)
admin.site.register(models.Projet)
admin.site.register(models.Service)
admin.site.register(models.Recensement)




# class BandAdmin(admin.ModelAdmin):
#     list_display = ('name', 'year_formed', 'genre') 

# admin.site.register(Band, BandAdmin)