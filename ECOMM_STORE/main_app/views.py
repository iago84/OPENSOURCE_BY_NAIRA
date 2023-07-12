from django.shortcuts import render

# Create your views here.

from rest_framework import serializers, generics

from django.views.generic import *
from rest_framework.generics import *
from rest_framework.views import *
from main_app.models import *
from main_app.serializers import *
from main_app.forms import *
class Index(TemplateView):
	template_name = 'index.html'
	
	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		return context


class PRODUCTS_CREATEVIEW(CreateView):
	template_name = 'PRODUCTS_create.html'
	model = PRODUCTS
	
	form_class = PRODUCTS_MF
	
	def get_context_data(self, **kwargs):
		context = super(PRODUCTS_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class CARTS_CREATEVIEW(CreateView):
	template_name = 'CARTS_create.html'
	model = CARTS
	
	form_class = CARTS_MF
	
	def get_context_data(self, **kwargs):
		context = super(CARTS_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class SURVEY_CREATEVIEW(CreateView):
	template_name = 'SURVEY_create.html'
	model = SURVEY
	
	form_class = SURVEY_MF
	
	def get_context_data(self, **kwargs):
		context = super(SURVEY_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class PRODUCTS_LISTVIEW(ListView):
	template_name = 'PRODUCTS_list.html'
	model = PRODUCTS
	
	def get_context_data(self, **kwargs):
		context = super(PRODUCTS_LISTVIEW, self).get_context_data(**kwargs)
		return context

class CARTS_LISTVIEW(ListView):
	template_name = 'CARTS_list.html'
	model = CARTS
	
	def get_context_data(self, **kwargs):
		context = super(CARTS_LISTVIEW, self).get_context_data(**kwargs)
		return context

class SURVEY_LISTVIEW(ListView):
	template_name = 'SURVEY_list.html'
	model = SURVEY
	
	def get_context_data(self, **kwargs):
		context = super(SURVEY_LISTVIEW, self).get_context_data(**kwargs)
		return context

class PRODUCTS_UPDATEVIEW(UpdateView):
	template_name = 'PRODUCTS_update.html'
	model = PRODUCTS
	
	form_class = PRODUCTS_MF
	
	def get_context_data(self, **kwargs):
		context = super(PRODUCTS_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class CARTS_UPDATEVIEW(UpdateView):
	template_name = 'CARTS_update.html'
	model = CARTS
	
	form_class = CARTS_MF
	
	def get_context_data(self, **kwargs):
		context = super(CARTS_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class SURVEY_UPDATEVIEW(UpdateView):
	template_name = 'SURVEY_update.html'
	model = SURVEY
	
	form_class = SURVEY_MF
	
	def get_context_data(self, **kwargs):
		context = super(SURVEY_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class PRODUCTS_DETAILVIEW(DetailView):
	template_name = 'PRODUCTS_detail.html'
	model = PRODUCTS
	
	def get_context_data(self, **kwargs):
		context = super(PRODUCTS_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class CARTS_DETAILVIEW(DetailView):
	template_name = 'CARTS_detail.html'
	model = CARTS
	
	def get_context_data(self, **kwargs):
		context = super(CARTS_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class SURVEY_DETAILVIEW(DetailView):
	template_name = 'SURVEY_detail.html'
	model = SURVEY
	
	def get_context_data(self, **kwargs):
		context = super(SURVEY_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class PRODUCTS_DELETEVIEW(DeleteView):
	template_name = 'PRODUCTS_direct-delete.html'
	model = PRODUCTS
	
	def get_context_data(self, **kwargs):
		context = super(PRODUCTS_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class CARTS_DELETEVIEW(DeleteView):
	template_name = 'CARTS_direct-delete.html'
	model = CARTS
	
	def get_context_data(self, **kwargs):
		context = super(CARTS_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class SURVEY_DELETEVIEW(DeleteView):
	template_name = 'SURVEY_direct-delete.html'
	model = SURVEY
	
	def get_context_data(self, **kwargs):
		context = super(SURVEY_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class PRODUCTSSerializerAPIView(APIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = PRODUCTS.objects.all() 

class PRODUCTSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = PRODUCTS.objects.all() 

class PRODUCTSSerializerListAPIView(ListAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = PRODUCTS.objects.all() 

class PRODUCTSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = PRODUCTS.objects.all() 

class PRODUCTSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = PRODUCTS.objects.all() 

class PRODUCTSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = PRODUCTS.objects.all() 

class PRODUCTSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = PRODUCTS.objects.all() 

class PRODUCTSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = PRODUCTS.objects.all() 

class PRODUCTSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = PRODUCTS.objects.all() 

class PRODUCTSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = PRODUCTS.objects.all() 

class PRODUCTSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = PRODUCTS.objects.all() 

class CARTSSerializerAPIView(APIView): 
    serializer_class = CARTSSerializer 
    queryset = PRODUCTS.objects.all() 

class CARTSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = CARTSSerializer 
    queryset = PRODUCTS.objects.all() 

class CARTSSerializerListAPIView(ListAPIView): 
    serializer_class = CARTSSerializer 
    queryset = PRODUCTS.objects.all() 

class CARTSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = CARTSSerializer 
    queryset = PRODUCTS.objects.all() 

class CARTSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = PRODUCTS.objects.all() 

class CARTSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = PRODUCTS.objects.all() 

class CARTSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = CARTSSerializer 
    queryset = PRODUCTS.objects.all() 

class CARTSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = PRODUCTS.objects.all() 

class CARTSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = PRODUCTS.objects.all() 

class CARTSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = CARTSSerializer 
    queryset = PRODUCTS.objects.all() 

class CARTSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = CARTSSerializer 
    queryset = PRODUCTS.objects.all() 

class SURVEYSerializerAPIView(APIView): 
    serializer_class = SURVEYSerializer 
    queryset = PRODUCTS.objects.all() 

class SURVEYSerializerGenericAPIView(GenericAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = PRODUCTS.objects.all() 

class SURVEYSerializerListAPIView(ListAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = PRODUCTS.objects.all() 

class SURVEYSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = PRODUCTS.objects.all() 

class SURVEYSerializerCreateAPIView(CreateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = PRODUCTS.objects.all() 

class SURVEYSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = PRODUCTS.objects.all() 

class SURVEYSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = PRODUCTS.objects.all() 

class SURVEYSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = PRODUCTS.objects.all() 

class SURVEYSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = PRODUCTS.objects.all() 

class SURVEYSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = PRODUCTS.objects.all() 

class SURVEYSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = PRODUCTS.objects.all() 

class PRODUCTSSerializerAPIView(APIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = CARTS.objects.all() 

class PRODUCTSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = CARTS.objects.all() 

class PRODUCTSSerializerListAPIView(ListAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = CARTS.objects.all() 

class PRODUCTSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = CARTS.objects.all() 

class PRODUCTSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = CARTS.objects.all() 

class PRODUCTSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = CARTS.objects.all() 

class PRODUCTSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = CARTS.objects.all() 

class PRODUCTSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = CARTS.objects.all() 

class PRODUCTSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = CARTS.objects.all() 

class PRODUCTSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = CARTS.objects.all() 

class PRODUCTSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = CARTS.objects.all() 

class CARTSSerializerAPIView(APIView): 
    serializer_class = CARTSSerializer 
    queryset = CARTS.objects.all() 

class CARTSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = CARTSSerializer 
    queryset = CARTS.objects.all() 

class CARTSSerializerListAPIView(ListAPIView): 
    serializer_class = CARTSSerializer 
    queryset = CARTS.objects.all() 

class CARTSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = CARTSSerializer 
    queryset = CARTS.objects.all() 

class CARTSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = CARTS.objects.all() 

class CARTSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = CARTS.objects.all() 

class CARTSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = CARTSSerializer 
    queryset = CARTS.objects.all() 

class CARTSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = CARTS.objects.all() 

class CARTSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = CARTS.objects.all() 

class CARTSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = CARTSSerializer 
    queryset = CARTS.objects.all() 

class CARTSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = CARTSSerializer 
    queryset = CARTS.objects.all() 

class SURVEYSerializerAPIView(APIView): 
    serializer_class = SURVEYSerializer 
    queryset = CARTS.objects.all() 

class SURVEYSerializerGenericAPIView(GenericAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = CARTS.objects.all() 

class SURVEYSerializerListAPIView(ListAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = CARTS.objects.all() 

class SURVEYSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = CARTS.objects.all() 

class SURVEYSerializerCreateAPIView(CreateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = CARTS.objects.all() 

class SURVEYSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = CARTS.objects.all() 

class SURVEYSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = CARTS.objects.all() 

class SURVEYSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = CARTS.objects.all() 

class SURVEYSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = CARTS.objects.all() 

class SURVEYSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = CARTS.objects.all() 

class SURVEYSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = CARTS.objects.all() 

class PRODUCTSSerializerAPIView(APIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = SURVEY.objects.all() 

class PRODUCTSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = SURVEY.objects.all() 

class PRODUCTSSerializerListAPIView(ListAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = SURVEY.objects.all() 

class PRODUCTSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = SURVEY.objects.all() 

class PRODUCTSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = SURVEY.objects.all() 

class PRODUCTSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = SURVEY.objects.all() 

class PRODUCTSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = SURVEY.objects.all() 

class PRODUCTSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = SURVEY.objects.all() 

class PRODUCTSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = SURVEY.objects.all() 

class PRODUCTSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = SURVEY.objects.all() 

class PRODUCTSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PRODUCTSSerializer 
    queryset = SURVEY.objects.all() 

class CARTSSerializerAPIView(APIView): 
    serializer_class = CARTSSerializer 
    queryset = SURVEY.objects.all() 

class CARTSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = CARTSSerializer 
    queryset = SURVEY.objects.all() 

class CARTSSerializerListAPIView(ListAPIView): 
    serializer_class = CARTSSerializer 
    queryset = SURVEY.objects.all() 

class CARTSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = CARTSSerializer 
    queryset = SURVEY.objects.all() 

class CARTSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = SURVEY.objects.all() 

class CARTSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = SURVEY.objects.all() 

class CARTSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = CARTSSerializer 
    queryset = SURVEY.objects.all() 

class CARTSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = SURVEY.objects.all() 

class CARTSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = CARTSSerializer 
    queryset = SURVEY.objects.all() 

class CARTSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = CARTSSerializer 
    queryset = SURVEY.objects.all() 

class CARTSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = CARTSSerializer 
    queryset = SURVEY.objects.all() 

class SURVEYSerializerAPIView(APIView): 
    serializer_class = SURVEYSerializer 
    queryset = SURVEY.objects.all() 

class SURVEYSerializerGenericAPIView(GenericAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = SURVEY.objects.all() 

class SURVEYSerializerListAPIView(ListAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = SURVEY.objects.all() 

class SURVEYSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = SURVEY.objects.all() 

class SURVEYSerializerCreateAPIView(CreateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = SURVEY.objects.all() 

class SURVEYSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = SURVEY.objects.all() 

class SURVEYSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = SURVEY.objects.all() 

class SURVEYSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = SURVEY.objects.all() 

class SURVEYSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = SURVEY.objects.all() 

class SURVEYSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = SURVEY.objects.all() 

class SURVEYSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = SURVEYSerializer 
    queryset = SURVEY.objects.all() 

