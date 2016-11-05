from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''https://docs.djangoproject.com/en/1.10/ref/models/fields/#model-field-types'''
class Person(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)

    birthday = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(
        max_length=2,
        choices=(('M', 'Male'), ('F', 'female'))
    )

    #  home

    def __str__(self):
    	return "%s %s" % (self.firstname, self.lastname)

    class Meta:
        abstract = True


class Child(Person):

    race = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    image = models.ImageField(upload_to='child_selfie')


class Staff(Person):
	phone = models.CharField(max_length=20)


class Relative(Person):
	phone = models.CharField(max_length=20)
	#relatedTo = models.ManyToManyField(Child)
	relatedTo = models.ForeignKey(Child)
	relationship = models.CharField(max_length=20)

class Home(models.Model):
	name = models.CharField(max_length=20)
	children = models.ManyToManyField(Child)
	director = models.CharField(max_length=20, default='')
	social_worker = models.CharField(max_length=20, default='')
	organization = models.CharField(max_length=50, default='')
	staff_in_charge = models.CharField(max_length=20, default='')
	parent_home = models.CharField(max_length=20, default='')

	def __str__(self):
		return name