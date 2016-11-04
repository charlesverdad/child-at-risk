from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''https://docs.djangoproject.com/en/1.10/ref/models/fields/#model-field-types'''


class Child(models.Model):
	firstname = models.CharField(max_length=50)
	middlename = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	nickname = models.CharField(max_length=50)
	
	birthday = models.DateField()
	gender = models.CharField(
		max_length=2,
		choices=(('M', 'Male'), ('F', 'female'))
	)
	race = models.CharField(max_length=50)
	religion = models.CharField(max_length=50)
	nationality = models.CharField(max_length=50)
	image = models.ImageField(upload_to='child_selfie')

	# home