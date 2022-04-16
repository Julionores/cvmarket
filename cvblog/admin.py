from django.contrib import admin

# Register your models here.

# Register your models here.

from cvblog.models import Cv, Lettre, Contact

#admin.site.register(Cv)
#admin.site.register(Lettre)
#admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('nomuser','deactive','date_created',) # liste les champs que nous voulons sur l'affichage de la liste
    search_fields = ('nomuser',)
    list_filter = ('date_edit','date_created','deactive',)
    readonly_fields = ('nomuser','date_edit',)
    

admin.site.register(Contact, ContactAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument

class CvAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('nomcv', 'usercv','date_created',) # liste les champs que nous voulons sur l'affichage de la liste
    search_fields = ('nomcv',)
    list_filter = ('date_edit','date_created',)
    readonly_fields = ('date_edit',)
    

admin.site.register(Cv, CvAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument

class LettreAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('usercv','destinateur','objet','date_created',) # liste les champs que nous voulons sur l'affichage de la liste
    search_fields = ('destinataire',)
    list_filter = ('date_edit','date_created',)
    readonly_fields = ('date_edit',)
    

admin.site.register(Lettre, LettreAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument

"""
class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')  # ajouter ‘band' ici

admin.site.register(Listing, ListingAdmin)"""