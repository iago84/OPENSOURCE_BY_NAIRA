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

class TASK_CREATEVIEW(CreateView):
	template_name = 'TASK_create.html'
	model = TASK
	
	form_class = TASK_MF
	
	def get_context_data(self, **kwargs):
		context = super(TASK_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class TAGS_CREATEVIEW(CreateView):
	template_name = 'TAGS_create.html'
	model = TAGS
	
	form_class = TAGS_MF
	
	def get_context_data(self, **kwargs):
		context = super(TAGS_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class ASSIGNATION_CREATEVIEW(CreateView):
	template_name = 'ASSIGNATION_create.html'
	model = ASSIGNATION
	
	form_class = ASSIGNATION_MF
	
	def get_context_data(self, **kwargs):
		context = super(ASSIGNATION_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class PROFILE_LISTVIEW(ListView):
	template_name = 'PROFILE_list.html'
	model = PROFILE
	
	def get_context_data(self, **kwargs):
		context = super(PROFILE_LISTVIEW, self).get_context_data(**kwargs)
		return context

class TASK_LISTVIEW(ListView):
	template_name = 'TASK_list.html'
	model = TASK
	
	def get_context_data(self, **kwargs):
		context = super(TASK_LISTVIEW, self).get_context_data(**kwargs)
		return context

class TAGS_LISTVIEW(ListView):
	template_name = 'TAGS_list.html'
	model = TAGS
	
	def get_context_data(self, **kwargs):
		context = super(TAGS_LISTVIEW, self).get_context_data(**kwargs)
		return context

class ASSIGNATION_LISTVIEW(ListView):
	template_name = 'ASSIGNATION_list.html'
	model = ASSIGNATION
	
	def get_context_data(self, **kwargs):
		context = super(ASSIGNATION_LISTVIEW, self).get_context_data(**kwargs)
		return context

class PROFILE_UPDATEVIEW(UpdateView):
	template_name = 'PROFILE_update.html'
	model = PROFILE
	
	form_class = PROFILE_MF
	
	def get_context_data(self, **kwargs):
		context = super(PROFILE_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class TASK_UPDATEVIEW(UpdateView):
	template_name = 'TASK_update.html'
	model = TASK
	
	form_class = TASK_MF
	
	def get_context_data(self, **kwargs):
		context = super(TASK_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class TAGS_UPDATEVIEW(UpdateView):
	template_name = 'TAGS_update.html'
	model = TAGS
	
	form_class = TAGS_MF
	
	def get_context_data(self, **kwargs):
		context = super(TAGS_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class ASSIGNATION_UPDATEVIEW(UpdateView):
	template_name = 'ASSIGNATION_update.html'
	model = ASSIGNATION
	
	form_class = ASSIGNATION_MF
	
	def get_context_data(self, **kwargs):
		context = super(ASSIGNATION_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class PROFILE_DETAILVIEW(DetailView):
	template_name = 'PROFILE_detail.html'
	model = PROFILE
	
	def get_context_data(self, **kwargs):
		context = super(PROFILE_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class TASK_DETAILVIEW(DetailView):
	template_name = 'TASK_detail.html'
	model = TASK
	
	def get_context_data(self, **kwargs):
		context = super(TASK_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class TAGS_DETAILVIEW(DetailView):
	template_name = 'TAGS_detail.html'
	model = TAGS
	
	def get_context_data(self, **kwargs):
		context = super(TAGS_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class ASSIGNATION_DETAILVIEW(DetailView):
	template_name = 'ASSIGNATION_detail.html'
	model = ASSIGNATION
	
	def get_context_data(self, **kwargs):
		context = super(ASSIGNATION_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class PROFILE_DELETEVIEW(DeleteView):
	template_name = 'PROFILE_direct-delete.html'
	model = PROFILE
	
	def get_context_data(self, **kwargs):
		context = super(PROFILE_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class TASK_DELETEVIEW(DeleteView):
	template_name = 'TASK_direct-delete.html'
	model = TASK
	
	def get_context_data(self, **kwargs):
		context = super(TASK_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class TAGS_DELETEVIEW(DeleteView):
	template_name = 'TAGS_direct-delete.html'
	model = TAGS
	
	def get_context_data(self, **kwargs):
		context = super(TAGS_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class ASSIGNATION_DELETEVIEW(DeleteView):
	template_name = 'ASSIGNATION_direct-delete.html'
	model = ASSIGNATION
	
	def get_context_data(self, **kwargs):
		context = super(ASSIGNATION_DELETEVIEW, self).get_context_data(**kwargs)
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

class TASKSerializerAPIView(APIView): 
    serializer_class = TASKSerializer 
    queryset = PROFILE.objects.all() 

class TASKSerializerGenericAPIView(GenericAPIView): 
    serializer_class = TASKSerializer 
    queryset = PROFILE.objects.all() 

class TASKSerializerListAPIView(ListAPIView): 
    serializer_class = TASKSerializer 
    queryset = PROFILE.objects.all() 

class TASKSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = TASKSerializer 
    queryset = PROFILE.objects.all() 

class TASKSerializerCreateAPIView(CreateAPIView): 
    serializer_class = TASKSerializer 
    queryset = PROFILE.objects.all() 

class TASKSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = TASKSerializer 
    queryset = PROFILE.objects.all() 

class TASKSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = TASKSerializer 
    queryset = PROFILE.objects.all() 

class TASKSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = TASKSerializer 
    queryset = PROFILE.objects.all() 

class TASKSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = TASKSerializer 
    queryset = PROFILE.objects.all() 

class TASKSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = TASKSerializer 
    queryset = PROFILE.objects.all() 

class TASKSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = TASKSerializer 
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

class ASSIGNATIONSerializerAPIView(APIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = PROFILE.objects.all() 

class ASSIGNATIONSerializerGenericAPIView(GenericAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = PROFILE.objects.all() 

class ASSIGNATIONSerializerListAPIView(ListAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = PROFILE.objects.all() 

class ASSIGNATIONSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = PROFILE.objects.all() 

class ASSIGNATIONSerializerCreateAPIView(CreateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = PROFILE.objects.all() 

class ASSIGNATIONSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = PROFILE.objects.all() 

class ASSIGNATIONSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = PROFILE.objects.all() 

class ASSIGNATIONSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = PROFILE.objects.all() 

class ASSIGNATIONSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = PROFILE.objects.all() 

class ASSIGNATIONSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = PROFILE.objects.all() 

class ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = PROFILE.objects.all() 

class PROFILESerializerAPIView(APIView): 
    serializer_class = PROFILESerializer 
    queryset = TASK.objects.all() 

class PROFILESerializerGenericAPIView(GenericAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TASK.objects.all() 

class PROFILESerializerListAPIView(ListAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TASK.objects.all() 

class PROFILESerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TASK.objects.all() 

class PROFILESerializerCreateAPIView(CreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TASK.objects.all() 

class PROFILESerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TASK.objects.all() 

class PROFILESerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TASK.objects.all() 

class PROFILESerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TASK.objects.all() 

class PROFILESerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TASK.objects.all() 

class PROFILESerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TASK.objects.all() 

class PROFILESerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = TASK.objects.all() 

class TASKSerializerAPIView(APIView): 
    serializer_class = TASKSerializer 
    queryset = TASK.objects.all() 

class TASKSerializerGenericAPIView(GenericAPIView): 
    serializer_class = TASKSerializer 
    queryset = TASK.objects.all() 

class TASKSerializerListAPIView(ListAPIView): 
    serializer_class = TASKSerializer 
    queryset = TASK.objects.all() 

class TASKSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = TASKSerializer 
    queryset = TASK.objects.all() 

class TASKSerializerCreateAPIView(CreateAPIView): 
    serializer_class = TASKSerializer 
    queryset = TASK.objects.all() 

class TASKSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = TASKSerializer 
    queryset = TASK.objects.all() 

class TASKSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = TASKSerializer 
    queryset = TASK.objects.all() 

class TASKSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = TASKSerializer 
    queryset = TASK.objects.all() 

class TASKSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = TASKSerializer 
    queryset = TASK.objects.all() 

class TASKSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = TASKSerializer 
    queryset = TASK.objects.all() 

class TASKSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = TASKSerializer 
    queryset = TASK.objects.all() 

class TAGSSerializerAPIView(APIView): 
    serializer_class = TAGSSerializer 
    queryset = TASK.objects.all() 

class TAGSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TASK.objects.all() 

class TAGSSerializerListAPIView(ListAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TASK.objects.all() 

class TAGSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TASK.objects.all() 

class TAGSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TASK.objects.all() 

class TAGSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TASK.objects.all() 

class TAGSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TASK.objects.all() 

class TAGSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TASK.objects.all() 

class TAGSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TASK.objects.all() 

class TAGSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TASK.objects.all() 

class TAGSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = TASK.objects.all() 

class ASSIGNATIONSerializerAPIView(APIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TASK.objects.all() 

class ASSIGNATIONSerializerGenericAPIView(GenericAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TASK.objects.all() 

class ASSIGNATIONSerializerListAPIView(ListAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TASK.objects.all() 

class ASSIGNATIONSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TASK.objects.all() 

class ASSIGNATIONSerializerCreateAPIView(CreateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TASK.objects.all() 

class ASSIGNATIONSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TASK.objects.all() 

class ASSIGNATIONSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TASK.objects.all() 

class ASSIGNATIONSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TASK.objects.all() 

class ASSIGNATIONSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TASK.objects.all() 

class ASSIGNATIONSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TASK.objects.all() 

class ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TASK.objects.all() 

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

class TASKSerializerAPIView(APIView): 
    serializer_class = TASKSerializer 
    queryset = TAGS.objects.all() 

class TASKSerializerGenericAPIView(GenericAPIView): 
    serializer_class = TASKSerializer 
    queryset = TAGS.objects.all() 

class TASKSerializerListAPIView(ListAPIView): 
    serializer_class = TASKSerializer 
    queryset = TAGS.objects.all() 

class TASKSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = TASKSerializer 
    queryset = TAGS.objects.all() 

class TASKSerializerCreateAPIView(CreateAPIView): 
    serializer_class = TASKSerializer 
    queryset = TAGS.objects.all() 

class TASKSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = TASKSerializer 
    queryset = TAGS.objects.all() 

class TASKSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = TASKSerializer 
    queryset = TAGS.objects.all() 

class TASKSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = TASKSerializer 
    queryset = TAGS.objects.all() 

class TASKSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = TASKSerializer 
    queryset = TAGS.objects.all() 

class TASKSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = TASKSerializer 
    queryset = TAGS.objects.all() 

class TASKSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = TASKSerializer 
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

class ASSIGNATIONSerializerAPIView(APIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TAGS.objects.all() 

class ASSIGNATIONSerializerGenericAPIView(GenericAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TAGS.objects.all() 

class ASSIGNATIONSerializerListAPIView(ListAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TAGS.objects.all() 

class ASSIGNATIONSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TAGS.objects.all() 

class ASSIGNATIONSerializerCreateAPIView(CreateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TAGS.objects.all() 

class ASSIGNATIONSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TAGS.objects.all() 

class ASSIGNATIONSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TAGS.objects.all() 

class ASSIGNATIONSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TAGS.objects.all() 

class ASSIGNATIONSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TAGS.objects.all() 

class ASSIGNATIONSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TAGS.objects.all() 

class ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = TAGS.objects.all() 

class PROFILESerializerAPIView(APIView): 
    serializer_class = PROFILESerializer 
    queryset = ASSIGNATION.objects.all() 

class PROFILESerializerGenericAPIView(GenericAPIView): 
    serializer_class = PROFILESerializer 
    queryset = ASSIGNATION.objects.all() 

class PROFILESerializerListAPIView(ListAPIView): 
    serializer_class = PROFILESerializer 
    queryset = ASSIGNATION.objects.all() 

class PROFILESerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = PROFILESerializer 
    queryset = ASSIGNATION.objects.all() 

class PROFILESerializerCreateAPIView(CreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = ASSIGNATION.objects.all() 

class PROFILESerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = ASSIGNATION.objects.all() 

class PROFILESerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = ASSIGNATION.objects.all() 

class PROFILESerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = ASSIGNATION.objects.all() 

class PROFILESerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = PROFILESerializer 
    queryset = ASSIGNATION.objects.all() 

class PROFILESerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = ASSIGNATION.objects.all() 

class PROFILESerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = PROFILESerializer 
    queryset = ASSIGNATION.objects.all() 

class TASKSerializerAPIView(APIView): 
    serializer_class = TASKSerializer 
    queryset = ASSIGNATION.objects.all() 

class TASKSerializerGenericAPIView(GenericAPIView): 
    serializer_class = TASKSerializer 
    queryset = ASSIGNATION.objects.all() 

class TASKSerializerListAPIView(ListAPIView): 
    serializer_class = TASKSerializer 
    queryset = ASSIGNATION.objects.all() 

class TASKSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = TASKSerializer 
    queryset = ASSIGNATION.objects.all() 

class TASKSerializerCreateAPIView(CreateAPIView): 
    serializer_class = TASKSerializer 
    queryset = ASSIGNATION.objects.all() 

class TASKSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = TASKSerializer 
    queryset = ASSIGNATION.objects.all() 

class TASKSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = TASKSerializer 
    queryset = ASSIGNATION.objects.all() 

class TASKSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = TASKSerializer 
    queryset = ASSIGNATION.objects.all() 

class TASKSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = TASKSerializer 
    queryset = ASSIGNATION.objects.all() 

class TASKSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = TASKSerializer 
    queryset = ASSIGNATION.objects.all() 

class TASKSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = TASKSerializer 
    queryset = ASSIGNATION.objects.all() 

class TAGSSerializerAPIView(APIView): 
    serializer_class = TAGSSerializer 
    queryset = ASSIGNATION.objects.all() 

class TAGSSerializerGenericAPIView(GenericAPIView): 
    serializer_class = TAGSSerializer 
    queryset = ASSIGNATION.objects.all() 

class TAGSSerializerListAPIView(ListAPIView): 
    serializer_class = TAGSSerializer 
    queryset = ASSIGNATION.objects.all() 

class TAGSSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = TAGSSerializer 
    queryset = ASSIGNATION.objects.all() 

class TAGSSerializerCreateAPIView(CreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = ASSIGNATION.objects.all() 

class TAGSSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = ASSIGNATION.objects.all() 

class TAGSSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = ASSIGNATION.objects.all() 

class TAGSSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = ASSIGNATION.objects.all() 

class TAGSSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = TAGSSerializer 
    queryset = ASSIGNATION.objects.all() 

class TAGSSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = ASSIGNATION.objects.all() 

class TAGSSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = TAGSSerializer 
    queryset = ASSIGNATION.objects.all() 

class ASSIGNATIONSerializerAPIView(APIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = ASSIGNATION.objects.all() 

class ASSIGNATIONSerializerGenericAPIView(GenericAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = ASSIGNATION.objects.all() 

class ASSIGNATIONSerializerListAPIView(ListAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = ASSIGNATION.objects.all() 

class ASSIGNATIONSerializerRetrieveAPIView(RetrieveAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = ASSIGNATION.objects.all() 

class ASSIGNATIONSerializerCreateAPIView(CreateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = ASSIGNATION.objects.all() 

class ASSIGNATIONSerializerUpdateAPIView(UpdateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = ASSIGNATION.objects.all() 

class ASSIGNATIONSerializerDestroyAPIView(DestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = ASSIGNATION.objects.all() 

class ASSIGNATIONSerializerListCreateAPIView(ListCreateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = ASSIGNATION.objects.all() 

class ASSIGNATIONSerializerRetrieveUpdateAPIView(RetrieveUpdateAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = ASSIGNATION.objects.all() 

class ASSIGNATIONSerializerRetrieveDestroyAPIView(RetrieveDestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = ASSIGNATION.objects.all() 

class ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = ASSIGNATIONSerializer 
    queryset = ASSIGNATION.objects.all() 

