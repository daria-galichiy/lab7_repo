from django.contrib import admin
from lab6.apps.db_app.models import *

# Register your models here.


class FilmsAdmin(admin.ModelAdmin):
    fields = ('film_name', 'release_date', 'in_the_lead_role', 'filmmaker', 'film_writer', 'producer', 'cameraman',
              'country', 'box_office_results')
    list_filter = ('release_date', 'country', ('in_the_lead_role', admin.RelatedOnlyFieldListFilter),)
    list_display = ('film_name', 'release_date', 'get_actors', 'filmmaker', 'film_writer', 'producer',
                    'cameraman', 'country', 'box_office_results')
    search_fields = ('film_name',)
    list_per_page = 10


class ActorsAdmin(admin.ModelAdmin):
    list_per_page = 10


admin.site.register(Actors, ActorsAdmin)
admin.site.register(Films, FilmsAdmin)

admin.site.site_url = '/main/'
admin.site.site_header = 'Django-администрирование'
admin.site.index_title = 'Администрирование'
