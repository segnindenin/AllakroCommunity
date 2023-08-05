from django.contrib import admin

# Register your models here.

from exchange.models import Habitant, Acteur, Communauty, Activity, Projet, ReferentielMetier, joboffer, Postulation, CarnetSante

class HabitantAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'nationality',
    'contact')
    
admin.site.register(Habitant, HabitantAdmin)
admin.site.register(Acteur)
admin.site.register(Activity)
admin.site.register(CarnetSante)
admin.site.register(ReferentielMetier)
admin.site.register(Communauty)
admin.site.register(joboffer)
admin.site.register(Postulation)
admin.site.register(Projet)




# class BandAdmin(admin.ModelAdmin):
#     list_display = ('name', 'year_formed', 'genre') 

# admin.site.register(Band, BandAdmin)