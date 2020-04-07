from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.utils.safestring import mark_safe

# city_choices = (
# 			("Indore" , "Indore"),("Dewas" , "Dewas"),("Ujjain" , "Ujjain"),("Ratlam" , "Ratlam"),
# 			("Agar" , "Agar"),("Neemuch" , "Neemuch"),("Dhar" , "Dhar"),("Jhabua" , "Jhabua"),
# 			("Mandsaur" , "Mandsaur"),("Rajgarh" , "Rajgarh"),("Guna" , "Guna"),("Sehore" , "Sehore"),
# 			("Jhalawar" , "Jhalawar"),("Banswara" , "Banswara"),("Chittorgarh" , "Chittorgarh"),
# 		)
class user_data(models.Model):
	name = models.CharField(max_length=100, default='buddy')
	email = models.EmailField(max_length = 70,blank=False)
	phone = models.IntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(6000000000)],blank=False)
	city= models.CharField(max_length=100,blank=False)
	message = models.TextField(max_length=250) 
	created_at = models.DateTimeField(auto_now_add=True)

class uploads_slider(models.Model):
	image = models.ImageField(default='default.jpg', upload_to='Profile_pics')
	img_name = models.CharField(max_length=100, default='')
	img_city= models.CharField(max_length=100,blank=False)
	uploded_at = models.DateTimeField(auto_now_add=True)

	def admin_photo(self):
		return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
		admin_photo.short_description = 'Image'
		admin_photo.allow_tags = True

		def __str__(self):
			return self.name


@receiver(pre_delete, sender=uploads_slider)
def uploads_slider_delete(sender, instance, **kwargs):
    instance.image.delete(False)