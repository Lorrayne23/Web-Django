from django.contrib import admin
from .models import Country,Cases

class EntryAdmin(admin.ModelAdmin):
    list_display = ["country", "confirmed","deaths" ,"recovered" ]


admin.site.register(Country)
admin.site.register(Cases,EntryAdmin)

