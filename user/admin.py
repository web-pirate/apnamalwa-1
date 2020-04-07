from django.contrib import admin
from user.models import *
from django.contrib.auth.models import Group

class DataAdmin(admin.ModelAdmin):
	list_display = ('name','city', 'email', 'phone')
	list_filter = ('city','created_at')

class ImageUp(admin.ModelAdmin):
	list_display = ('admin_photo','img_name', 'image', 'img_city', 'uploded_at')
	list_filter = ('img_name', 'img_city')


	# readonly_fields = ('admin_photo',)



admin.site.site_header = 'Apna Malwa Admin Page'
admin.site.register(user_data, DataAdmin)
admin.site.register(uploads_slider, ImageUp)

