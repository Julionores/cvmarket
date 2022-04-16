from django.contrib import admin
from cvblog.admin import ContactAdmin
from cvblog.models import Contact

# Register your models here.

# Register your models here.

from authentication.models import User

#admin.site.register(User)

class ContactInline(admin.TabularInline):
    model = Contact
    readonly_fields = ("nomuser","date_edit","date_created",)


class UserAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('username', 'email','is_staff','is_superuser','date_edit','date_created',) # liste les champs que nous voulons sur l'affichage de la liste
    search_fields = ('username', 'email')
    list_filter = ('date_edit','date_created',)
    readonly_fields = ('date_edit',)
    inlines = (ContactInline,)

admin.site.register(User, UserAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
