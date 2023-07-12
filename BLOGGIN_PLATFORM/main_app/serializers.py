from rest_framework import serializers
from main_app.models import *
class PROFILESerializer(serializers.ModelSerializer):
	class Meta:
		model = PROFILE
		fields = "__all__"

class PUBLICATIONSerializer(serializers.ModelSerializer):
	class Meta:
		model = PUBLICATION
		fields = "__all__"

class COMMENTSSerializer(serializers.ModelSerializer):
	class Meta:
		model = COMMENTS
		fields = "__all__"

class TAGSSerializer(serializers.ModelSerializer):
	class Meta:
		model = TAGS
		fields = "__all__"

