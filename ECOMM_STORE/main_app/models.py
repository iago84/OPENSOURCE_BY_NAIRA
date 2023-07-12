# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class PRODUCTS(models.Model):

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creacion', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificacion', auto_now=True, auto_now_add=False)

class CARTS(models.Model):

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creacion', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificacion', auto_now=True, auto_now_add=False)

class SURVEY(models.Model):

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creacion', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificacion', auto_now=True, auto_now_add=False)

