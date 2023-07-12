from rest_framework import serializers
from main_app.models import *
class PRODUCTSSerializer(serializers.ModelSerializer):
	class Meta:
		model = PRODUCTS
		fields = "__all__"

class CARTSSerializer(serializers.ModelSerializer):
	class Meta:
		model = CARTS
		fields = "__all__"

class SURVEYSerializer(serializers.ModelSerializer):
	class Meta:
		model = SURVEY
		fields = "__all__"

