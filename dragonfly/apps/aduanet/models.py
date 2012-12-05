# -*- coding: utf-8 -*-
from django.db import models

class Country (models.Model):
	code = models.CharField(max_length=5)
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name = u"País"
		verbose_name_plural = u"Países"

	def __unicode__(self):
		return "%s - %s" % (self.code, self.name)

class Regime(models.Model):
   code = models.CharField(max_length = 5)
   name = models.CharField(max_length = 30)

   def __unicode__(self):
		return "%s - %s" % (self.code, self.name)

class Aduana(models.Model):
   code = models.CharField(max_length=10)
   name = models.CharField(max_length=150)

   def __unicode__(self):
		return "%s - %s" % (self.code, self.name)
