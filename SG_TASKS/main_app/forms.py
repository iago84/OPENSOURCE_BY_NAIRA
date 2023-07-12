
from django.forms import ModelForm
from main_app.models import *

class PROFILE_MF(ModelForm):


	class Meta:

		model=PROFILE
		fields="__all__"

class TASK_MF(ModelForm):


	class Meta:

		model=TASK
		fields="__all__"

class TAGS_MF(ModelForm):


	class Meta:

		model=TAGS
		fields="__all__"

class ASSIGNATION_MF(ModelForm):


	class Meta:

		model=ASSIGNATION
		fields="__all__"

