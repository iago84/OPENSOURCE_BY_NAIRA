from rest_framework import serializers
from main_app.models import *
class PROFILESerializer(serializers.ModelSerializer):
	class Meta:
		model = PROFILE
		fields = "__all__"

class TASKSerializer(serializers.ModelSerializer):
	class Meta:
		model = TASK
		fields = "__all__"

class TAGSSerializer(serializers.ModelSerializer):
	class Meta:
		model = TAGS
		fields = "__all__"

class ASSIGNATIONSerializer(serializers.ModelSerializer):
	class Meta:
		model = ASSIGNATION
		fields = "__all__"

