from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Line(models.Model):
	name = models.TextField()
	owner = models.ForeignKey(User)
	def __str__(self):
			return self.name

class Issue(models.Model):
	lineid = models.ForeignKey(Line, on_delete=models.CASCADE)
	item = models.TextField(default=None)
	scrap = models.FloatField(default=None)
	status = models.TextField(default=None)
	openDate = models.DateField(default=None)
	rootCause = models.TextField(default=None)
	team = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	targetDate = models.DateField(default=None)
	closeDate = models.DateField(default=None)
	problem = models.TextField(default=None)

	def __str__(self):
		return self.problem
