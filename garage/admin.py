from django.contrib import admin
from .models import Car , CarImage

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display   = ('marke','modell','baujahr','preis')
    list_filter    = ('kraftstoffart','getriebe')
    search_fields  = ('marke','modell','vin')
    inlines = [CarImageInline]