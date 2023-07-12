
from django.forms import ModelForm
from main_app.models import *

class PRODUCTS_MF(ModelForm):


	class Meta:

		model=PRODUCTS
		fields="__all__"

class CARTS_MF(ModelForm):


	class Meta:

		model=CARTS
		fields="__all__"

class SURVEY_MF(ModelForm):


	class Meta:

		model=SURVEY
		fields="__all__"

