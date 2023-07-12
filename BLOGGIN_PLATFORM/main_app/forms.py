
from django.forms import ModelForm
from main_app.models import *

class PROFILE_MF(ModelForm):


	class Meta:

		model=PROFILE
		fields="__all__"

class PUBLICATION_MF(ModelForm):


	class Meta:

		model=PUBLICATION
		fields="__all__"

class COMMENTS_MF(ModelForm):


	class Meta:

		model=COMMENTS
		fields="__all__"

class TAGS_MF(ModelForm):


	class Meta:

		model=TAGS
		fields="__all__"

