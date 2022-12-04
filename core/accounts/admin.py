from django.contrib import admin
from .models import Listing, Property_Type, Prop_Status, Subdivision, Property_images


# Register your models here.
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('address', 'price')
    list_filter = ('address', 'price')
    search_fields = ('address', 'price', 'square_footage')

@admin.register(Property_Type)
class Property_TypeAdmin(admin.ModelAdmin):
    list_display = ('prop_type_name', 'prop_type_descr')

@admin.register(Prop_Status)
class Prop_StatusAdmin(admin.ModelAdmin):
    list_display = ('prop_status', 'prop_status_descr')

@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('subdiv_name', 'subdiv_descr')

@admin.register(Property_images)
class PropImagesAdmin(admin.ModelAdmin):
    list_display = ('prop_image_name', 'listing', 'image')