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


class PROFILE_CREATEVIEW(CreateView):
	template_name = 'PROFILE_create.html'
	model = PROFILE
	
	form_class = PROFILE_MF
	
	def get_context_data(self, **kwargs):
		context = super(PROFILE_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class PUBLICATION_CREATEVIEW(CreateView):
	template_name = 'PUBLICATION_create.html'
	model = PUBLICATION
	
	form_class = PUBLICATION_MF
	
	def get_context_data(self, **kwargs):
		context = super(PUBLICATION_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class COMMENTS_CREATEVIEW(CreateView):
	template_name = 'COMMENTS_create.html'
	model = COMMENTS
	
	form_class = COMMENTS_MF
	
	def get_context_data(self, **kwargs):
		context = super(COMMENTS_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class TAGS_CREATEVIEW(CreateView):
	template_name = 'TAGS_create.html'
	model = TAGS
	
	form_class = TAGS_MF
	
	def get_context_data(self, **kwargs):
		context = super(TAGS_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class PROFILE_LISTVIEW(ListView):
	template_name = 'PROFILE_list.html'
	model = PROFILE
	
	def get_context_data(self, **kwargs):
		context = super(PROFILE_LISTVIEW, self).get_context_data(**kwargs)
		return context

class PUBLICATION_LISTVIEW(ListView):
	template_name = 'PUBLICATION_list.html'
	model = PUBLICATION
	
	def get_context_data(self, **kwargs):
		context = super(PUBLICATION_LISTVIEW, self).get_context_data(**kwargs)
		return context

class COMMENTS_LISTVIEW(ListView):
	template_name = 'COMMENTS_list.html'
	model = COMMENTS
	
	def get_context_data(self, **kwargs):
		context = super(COMMENTS_LISTVIEW, self).get_context_data(**kwargs)
		return context

class TAGS_LISTVIEW(ListView):
	template_name = 'TAGS_list.html'
	model = TAGS
	
	def get_context_data(self, **kwargs):
		context = super(TAGS_LISTVIEW, self).get_context_data(**kwargs)
		return context

class PROFILE_UPDATEVIEW(UpdateView):
	template_name = 'PROFILE_update.html'
	model = PROFILE
	
	form_class = PROFILE_MF
	
	def get_context_data(self, **kwargs):
		context = super(PROFILE_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class PUBLICATION_UPDATEVIEW(UpdateView):
	template_name = 'PUBLICATION_update.html'
	model = PUBLICATION
	
	form_class = PUBLICATION_MF
	
	def get_context_data(self, **kwargs):
		context = super(PUBLICATION_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class COMMENTS_UPDATEVIEW(UpdateView):
	template_name = 'COMMENTS_update.html'
	model = COMMENTS
	
	form_class = COMMENTS_MF
	
	def get_context_data(self, **kwargs):
		context = super(COMMENTS_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class TAGS_UPDATEVIEW(UpdateView):
	template_name = 'TAGS_update.html'
	model = TAGS
	
	form_class = TAGS_MF
	
	def get_context_data(self, **kwargs):
		context = super(TAGS_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class PROFILE_DETAILVIEW(DetailView):
	template_name = 'PROFILE_detail.html'
	model = PROFILE
	
	def get_context_data(self, **kwargs):
		context = super(PROFILE_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class PUBLICATION_DETAILVIEW(DetailView):
	template_name = 'PUBLICATION_detail.html'
	model = PUBLICATION
	
	def get_context_data(self, **kwargs):
		context = super(PUBLICATION_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class COMMENTS_DETAILVIEW(DetailView):
	template_name = 'COMMENTS_detail.html'
	model = COMMENTS
	
	def get_context_data(self, **kwargs):
		context = super(COMMENTS_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class TAGS_DETAILVIEW(DetailView):
	template_name = 'TAGS_detail.html'
	model = TAGS
	
	def get_context_data(self, **kwargs):
		context = super(TAGS_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class PROFILE_DELETEVIEW(DeleteView):
	template_name = 'PROFILE_direct-delete.html'
	model = PROFILE
	
	def get_context_data(self, **kwargs):
		context = super(PROFILE_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class PUBLICATION_DELETEVIEW(DeleteView):
	template_name = 'PUBLICATION_direct-delete.html'
	model = PUBLICATION
	
	def get_context_data(self, **kwargs):
		context = super(PUBLICATION_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class COMMENTS_DELETEVIEW(DeleteView):
	template_name = 'COMMENTS_direct-delete.html'
	model = COMMENTS
	
	def get_context_data(self, **kwargs):
		context = super(COMMENTS_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class TAGS_DELETEVIEW(DeleteView):
	template_name = 'TAGS_direct-delete.html'
	model = TAGS
	
	def get_context_data(self, **kwargs):
		context = super(TAGS_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class PROFILESerializerAPIView(APIView): 
    serializer_class = PROFILESerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerGenericAPIView(GenericAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerListAPIView(ListAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerCreateAPIView(CreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PROFILE.objects.all() 

class PUBLICATIONSerializerAPIView(APIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PROFILE.objects.all() 

class PUBLICATIONSerializerGenericAPIView(GenericAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PROFILE.objects.all() 

class PUBLICATIONSerializerListAPIView(ListAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PROFILE.objects.all() 

class PUBLICATIONSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PROFILE.objects.all() 

class PUBLICATIONSerializerCreateAPIView(CreateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PROFILE.objects.all() 

class PUBLICATIONSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PROFILE.objects.all() 

class PUBLICATIONSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PROFILE.objects.all() 

class PUBLICATIONSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PROFILE.objects.all() 

class PUBLICATIONSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PROFILE.objects.all() 

class PUBLICATIONSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PROFILE.objects.all() 

class PUBLICATIONSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PROFILE.objects.all() 

class COMMENTSSerializerAPIView(APIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PROFILE.objects.all() 

class COMMENTSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PROFILE.objects.all() 

class COMMENTSSerializerListAPIView(ListAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PROFILE.objects.all() 

class COMMENTSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PROFILE.objects.all() 

class COMMENTSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PROFILE.objects.all() 

class COMMENTSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PROFILE.objects.all() 

class COMMENTSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PROFILE.objects.all() 

class COMMENTSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PROFILE.objects.all() 

class COMMENTSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PROFILE.objects.all() 

class COMMENTSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PROFILE.objects.all() 

class COMMENTSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PROFILE.objects.all() 

class TAGSSerializerAPIView(APIView): 
    serializer_class = TAGSSerializer 
    queryset = PROFILE.objects.all() 

class TAGSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PROFILE.objects.all() 

class TAGSSerializerListAPIView(ListAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PROFILE.objects.all() 

class TAGSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PROFILE.objects.all() 

class TAGSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PROFILE.objects.all() 

class TAGSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PROFILE.objects.all() 

class TAGSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PROFILE.objects.all() 

class TAGSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PROFILE.objects.all() 

class TAGSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PROFILE.objects.all() 

class TAGSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PROFILE.objects.all() 

class TAGSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerAPIView(APIView): 
    serializer_class = PROFILESerializer 
    queryset = PUBLICATION.objects.all() 

class PROFILESerializerGenericAPIView(GenericAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PUBLICATION.objects.all() 

class PROFILESerializerListAPIView(ListAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PUBLICATION.objects.all() 

class PROFILESerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PUBLICATION.objects.all() 

class PROFILESerializerCreateAPIView(CreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PUBLICATION.objects.all() 

class PROFILESerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PUBLICATION.objects.all() 

class PROFILESerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PUBLICATION.objects.all() 

class PROFILESerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PUBLICATION.objects.all() 

class PROFILESerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PUBLICATION.objects.all() 

class PROFILESerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PUBLICATION.objects.all() 

class PROFILESerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = PUBLICATION.objects.all() 

class PUBLICATIONSerializerAPIView(APIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PUBLICATION.objects.all() 

class PUBLICATIONSerializerGenericAPIView(GenericAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PUBLICATION.objects.all() 

class PUBLICATIONSerializerListAPIView(ListAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PUBLICATION.objects.all() 

class PUBLICATIONSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PUBLICATION.objects.all() 

class PUBLICATIONSerializerCreateAPIView(CreateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PUBLICATION.objects.all() 

class PUBLICATIONSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PUBLICATION.objects.all() 

class PUBLICATIONSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PUBLICATION.objects.all() 

class PUBLICATIONSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PUBLICATION.objects.all() 

class PUBLICATIONSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PUBLICATION.objects.all() 

class PUBLICATIONSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PUBLICATION.objects.all() 

class PUBLICATIONSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = PUBLICATION.objects.all() 

class COMMENTSSerializerAPIView(APIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PUBLICATION.objects.all() 

class COMMENTSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PUBLICATION.objects.all() 

class COMMENTSSerializerListAPIView(ListAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PUBLICATION.objects.all() 

class COMMENTSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PUBLICATION.objects.all() 

class COMMENTSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PUBLICATION.objects.all() 

class COMMENTSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PUBLICATION.objects.all() 

class COMMENTSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PUBLICATION.objects.all() 

class COMMENTSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PUBLICATION.objects.all() 

class COMMENTSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PUBLICATION.objects.all() 

class COMMENTSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PUBLICATION.objects.all() 

class COMMENTSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = PUBLICATION.objects.all() 

class TAGSSerializerAPIView(APIView): 
    serializer_class = TAGSSerializer 
    queryset = PUBLICATION.objects.all() 

class TAGSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PUBLICATION.objects.all() 

class TAGSSerializerListAPIView(ListAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PUBLICATION.objects.all() 

class TAGSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PUBLICATION.objects.all() 

class TAGSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PUBLICATION.objects.all() 

class TAGSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PUBLICATION.objects.all() 

class TAGSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PUBLICATION.objects.all() 

class TAGSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PUBLICATION.objects.all() 

class TAGSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PUBLICATION.objects.all() 

class TAGSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PUBLICATION.objects.all() 

class TAGSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = PUBLICATION.objects.all() 

class PROFILESerializerAPIView(APIView): 
    serializer_class = PROFILESerializer 
    queryset = COMMENTS.objects.all() 

class PROFILESerializerGenericAPIView(GenericAPIView): 
    serializer_class = PROFILESerializer 
    queryset = COMMENTS.objects.all() 

class PROFILESerializerListAPIView(ListAPIView): 
    serializer_class = PROFILESerializer 
    queryset = COMMENTS.objects.all() 

class PROFILESerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PROFILESerializer 
    queryset = COMMENTS.objects.all() 

class PROFILESerializerCreateAPIView(CreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = COMMENTS.objects.all() 

class PROFILESerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = COMMENTS.objects.all() 

class PROFILESerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = COMMENTS.objects.all() 

class PROFILESerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = COMMENTS.objects.all() 

class PROFILESerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = COMMENTS.objects.all() 

class PROFILESerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = COMMENTS.objects.all() 

class PROFILESerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = COMMENTS.objects.all() 

class PUBLICATIONSerializerAPIView(APIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = COMMENTS.objects.all() 

class PUBLICATIONSerializerGenericAPIView(GenericAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = COMMENTS.objects.all() 

class PUBLICATIONSerializerListAPIView(ListAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = COMMENTS.objects.all() 

class PUBLICATIONSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = COMMENTS.objects.all() 

class PUBLICATIONSerializerCreateAPIView(CreateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = COMMENTS.objects.all() 

class PUBLICATIONSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = COMMENTS.objects.all() 

class PUBLICATIONSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = COMMENTS.objects.all() 

class PUBLICATIONSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = COMMENTS.objects.all() 

class PUBLICATIONSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = COMMENTS.objects.all() 

class PUBLICATIONSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = COMMENTS.objects.all() 

class PUBLICATIONSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = COMMENTS.objects.all() 

class COMMENTSSerializerAPIView(APIView): 
    serializer_class = COMMENTSSerializer 
    queryset = COMMENTS.objects.all() 

class COMMENTSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = COMMENTS.objects.all() 

class COMMENTSSerializerListAPIView(ListAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = COMMENTS.objects.all() 

class COMMENTSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = COMMENTS.objects.all() 

class COMMENTSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = COMMENTS.objects.all() 

class COMMENTSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = COMMENTS.objects.all() 

class COMMENTSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = COMMENTS.objects.all() 

class COMMENTSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = COMMENTS.objects.all() 

class COMMENTSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = COMMENTS.objects.all() 

class COMMENTSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = COMMENTS.objects.all() 

class COMMENTSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = COMMENTS.objects.all() 

class TAGSSerializerAPIView(APIView): 
    serializer_class = TAGSSerializer 
    queryset = COMMENTS.objects.all() 

class TAGSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = TAGSSerializer 
    queryset = COMMENTS.objects.all() 

class TAGSSerializerListAPIView(ListAPIView): 
    serializer_class = TAGSSerializer 
    queryset = COMMENTS.objects.all() 

class TAGSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = TAGSSerializer 
    queryset = COMMENTS.objects.all() 

class TAGSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = COMMENTS.objects.all() 

class TAGSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = COMMENTS.objects.all() 

class TAGSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = COMMENTS.objects.all() 

class TAGSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = COMMENTS.objects.all() 

class TAGSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = COMMENTS.objects.all() 

class TAGSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = COMMENTS.objects.all() 

class TAGSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = COMMENTS.objects.all() 

class PROFILESerializerAPIView(APIView): 
    serializer_class = PROFILESerializer 
    queryset = TAGS.objects.all() 

class PROFILESerializerGenericAPIView(GenericAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TAGS.objects.all() 

class PROFILESerializerListAPIView(ListAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TAGS.objects.all() 

class PROFILESerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TAGS.objects.all() 

class PROFILESerializerCreateAPIView(CreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TAGS.objects.all() 

class PROFILESerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TAGS.objects.all() 

class PROFILESerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TAGS.objects.all() 

class PROFILESerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TAGS.objects.all() 

class PROFILESerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TAGS.objects.all() 

class PROFILESerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TAGS.objects.all() 

class PROFILESerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TAGS.objects.all() 

class PUBLICATIONSerializerAPIView(APIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = TAGS.objects.all() 

class PUBLICATIONSerializerGenericAPIView(GenericAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = TAGS.objects.all() 

class PUBLICATIONSerializerListAPIView(ListAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = TAGS.objects.all() 

class PUBLICATIONSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = TAGS.objects.all() 

class PUBLICATIONSerializerCreateAPIView(CreateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = TAGS.objects.all() 

class PUBLICATIONSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = TAGS.objects.all() 

class PUBLICATIONSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = TAGS.objects.all() 

class PUBLICATIONSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = TAGS.objects.all() 

class PUBLICATIONSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = TAGS.objects.all() 

class PUBLICATIONSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = TAGS.objects.all() 

class PUBLICATIONSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PUBLICATIONSerializer 
    queryset = TAGS.objects.all() 

class COMMENTSSerializerAPIView(APIView): 
    serializer_class = COMMENTSSerializer 
    queryset = TAGS.objects.all() 

class COMMENTSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = TAGS.objects.all() 

class COMMENTSSerializerListAPIView(ListAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = TAGS.objects.all() 

class COMMENTSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = TAGS.objects.all() 

class COMMENTSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = TAGS.objects.all() 

class COMMENTSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = TAGS.objects.all() 

class COMMENTSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = TAGS.objects.all() 

class COMMENTSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = TAGS.objects.all() 

class COMMENTSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = TAGS.objects.all() 

class COMMENTSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = TAGS.objects.all() 

class COMMENTSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = COMMENTSSerializer 
    queryset = TAGS.objects.all() 

class TAGSSerializerAPIView(APIView): 
    serializer_class = TAGSSerializer 
    queryset = TAGS.objects.all() 

class TAGSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TAGS.objects.all() 

class TAGSSerializerListAPIView(ListAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TAGS.objects.all() 

class TAGSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TAGS.objects.all() 

class TAGSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TAGS.objects.all() 

class TAGSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TAGS.objects.all() 

class TAGSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TAGS.objects.all() 

class TAGSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TAGS.objects.all() 

class TAGSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TAGS.objects.all() 

class TAGSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TAGS.objects.all() 

class TAGSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TAGS.objects.all() 

