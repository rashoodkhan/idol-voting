from django.db import models
from django.contrib.auth.models import User

class Participant(models.Model):
	name = models.CharField(max_length=100)
	picture = models.ImageField(verbose_name='Picture')
	vote_count = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	has_voted = models.BooleanField(default=False)

	def voted(self):
		return self.has_voted
