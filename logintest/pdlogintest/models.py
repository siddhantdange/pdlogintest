from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=15)
	birthday = models.DateTimeField()
	user_id = models.IntegerField()
	description = models.CharField(max_length=200)
	
	def __unicode__(self):
		return "ID: " + str(self.id) + "\nusername: " + str(self.username) + "\ndescription: " + str(self.description)


