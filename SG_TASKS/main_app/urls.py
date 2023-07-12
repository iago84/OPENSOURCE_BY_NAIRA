
from django.contrib import admin
from django.urls import path

from main_app.views import *
urlpatterns=[]
urlpatterns +=[path('',Index.as_view(),name='Index'),]
urlpatterns +=[path('PROFILE_CREATEVIEW',PROFILE_CREATEVIEW.as_view(),name='PROFILE_CREATEVIEW'),]

urlpatterns +=[path('TASK_CREATEVIEW',TASK_CREATEVIEW.as_view(),name='TASK_CREATEVIEW'),]

urlpatterns +=[path('TAGS_CREATEVIEW',TAGS_CREATEVIEW.as_view(),name='TAGS_CREATEVIEW'),]

urlpatterns +=[path('ASSIGNATION_CREATEVIEW',ASSIGNATION_CREATEVIEW.as_view(),name='ASSIGNATION_CREATEVIEW'),]

urlpatterns +=[path('PROFILE_LISTVIEW',PROFILE_LISTVIEW.as_view(),name='PROFILE_LISTVIEW'),]

urlpatterns +=[path('TASK_LISTVIEW',TASK_LISTVIEW.as_view(),name='TASK_LISTVIEW'),]

urlpatterns +=[path('TAGS_LISTVIEW',TAGS_LISTVIEW.as_view(),name='TAGS_LISTVIEW'),]

urlpatterns +=[path('ASSIGNATION_LISTVIEW',ASSIGNATION_LISTVIEW.as_view(),name='ASSIGNATION_LISTVIEW'),]

urlpatterns +=[path('PROFILE_UPDATEVIEW/<int:pk>',PROFILE_UPDATEVIEW.as_view(),name='PROFILE_UPDATEVIEW'),]

urlpatterns +=[path('TASK_UPDATEVIEW/<int:pk>',TASK_UPDATEVIEW.as_view(),name='TASK_UPDATEVIEW'),]

urlpatterns +=[path('TAGS_UPDATEVIEW/<int:pk>',TAGS_UPDATEVIEW.as_view(),name='TAGS_UPDATEVIEW'),]

urlpatterns +=[path('ASSIGNATION_UPDATEVIEW/<int:pk>',ASSIGNATION_UPDATEVIEW.as_view(),name='ASSIGNATION_UPDATEVIEW'),]

urlpatterns +=[path('PROFILE_DETAILVIEW/<int:pk>',PROFILE_DETAILVIEW.as_view(),name='PROFILE_DETAILVIEW'),]

urlpatterns +=[path('TASK_DETAILVIEW/<int:pk>',TASK_DETAILVIEW.as_view(),name='TASK_DETAILVIEW'),]

urlpatterns +=[path('TAGS_DETAILVIEW/<int:pk>',TAGS_DETAILVIEW.as_view(),name='TAGS_DETAILVIEW'),]

urlpatterns +=[path('ASSIGNATION_DETAILVIEW/<int:pk>',ASSIGNATION_DETAILVIEW.as_view(),name='ASSIGNATION_DETAILVIEW'),]

urlpatterns +=[path('PROFILE_DELETEVIEW/<int:pk>',PROFILE_DELETEVIEW.as_view(),name='PROFILE_DELETEVIEW'),]

urlpatterns +=[path('TASK_DELETEVIEW/<int:pk>',TASK_DELETEVIEW.as_view(),name='TASK_DELETEVIEW'),]

urlpatterns +=[path('TAGS_DELETEVIEW/<int:pk>',TAGS_DELETEVIEW.as_view(),name='TAGS_DELETEVIEW'),]

urlpatterns +=[path('ASSIGNATION_DELETEVIEW/<int:pk>',ASSIGNATION_DELETEVIEW.as_view(),name='ASSIGNATION_DELETEVIEW'),]

urlpatterns +=[path('PROFILESerializerAPIView',PROFILESerializerAPIView.as_view(),name='PROFILESerializerAPIView'),]

urlpatterns +=[path('PROFILESerializerGenericAPIView',PROFILESerializerGenericAPIView.as_view(),name='PROFILESerializerGenericAPIView'),]

urlpatterns +=[path('PROFILESerializerListAPIView',PROFILESerializerListAPIView.as_view(),name='PROFILESerializerListAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveAPIView',PROFILESerializerRetrieveAPIView.as_view(),name='PROFILESerializerRetrieveAPIView'),]

urlpatterns +=[path('PROFILESerializerCreateAPIView',PROFILESerializerCreateAPIView.as_view(),name='PROFILESerializerCreateAPIView'),]

urlpatterns +=[path('PROFILESerializerUpdateAPIView',PROFILESerializerUpdateAPIView.as_view(),name='PROFILESerializerUpdateAPIView'),]

urlpatterns +=[path('PROFILESerializerDestroyAPIView',PROFILESerializerDestroyAPIView.as_view(),name='PROFILESerializerDestroyAPIView'),]

urlpatterns +=[path('PROFILESerializerListCreateAPIView',PROFILESerializerListCreateAPIView.as_view(),name='PROFILESerializerListCreateAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveUpdateAPIView',PROFILESerializerRetrieveUpdateAPIView.as_view(),name='PROFILESerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveDestroyAPIView',PROFILESerializerRetrieveDestroyAPIView.as_view(),name='PROFILESerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveUpdateDestroyAPIView',PROFILESerializerRetrieveUpdateDestroyAPIView.as_view(),name='PROFILESerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerAPIView',TASKSerializerAPIView.as_view(),name='TASKSerializerAPIView'),]

urlpatterns +=[path('TASKSerializerGenericAPIView',TASKSerializerGenericAPIView.as_view(),name='TASKSerializerGenericAPIView'),]

urlpatterns +=[path('TASKSerializerListAPIView',TASKSerializerListAPIView.as_view(),name='TASKSerializerListAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveAPIView',TASKSerializerRetrieveAPIView.as_view(),name='TASKSerializerRetrieveAPIView'),]

urlpatterns +=[path('TASKSerializerCreateAPIView',TASKSerializerCreateAPIView.as_view(),name='TASKSerializerCreateAPIView'),]

urlpatterns +=[path('TASKSerializerUpdateAPIView',TASKSerializerUpdateAPIView.as_view(),name='TASKSerializerUpdateAPIView'),]

urlpatterns +=[path('TASKSerializerDestroyAPIView',TASKSerializerDestroyAPIView.as_view(),name='TASKSerializerDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerListCreateAPIView',TASKSerializerListCreateAPIView.as_view(),name='TASKSerializerListCreateAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveUpdateAPIView',TASKSerializerRetrieveUpdateAPIView.as_view(),name='TASKSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveDestroyAPIView',TASKSerializerRetrieveDestroyAPIView.as_view(),name='TASKSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveUpdateDestroyAPIView',TASKSerializerRetrieveUpdateDestroyAPIView.as_view(),name='TASKSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerAPIView',TAGSSerializerAPIView.as_view(),name='TAGSSerializerAPIView'),]

urlpatterns +=[path('TAGSSerializerGenericAPIView',TAGSSerializerGenericAPIView.as_view(),name='TAGSSerializerGenericAPIView'),]

urlpatterns +=[path('TAGSSerializerListAPIView',TAGSSerializerListAPIView.as_view(),name='TAGSSerializerListAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveAPIView',TAGSSerializerRetrieveAPIView.as_view(),name='TAGSSerializerRetrieveAPIView'),]

urlpatterns +=[path('TAGSSerializerCreateAPIView',TAGSSerializerCreateAPIView.as_view(),name='TAGSSerializerCreateAPIView'),]

urlpatterns +=[path('TAGSSerializerUpdateAPIView',TAGSSerializerUpdateAPIView.as_view(),name='TAGSSerializerUpdateAPIView'),]

urlpatterns +=[path('TAGSSerializerDestroyAPIView',TAGSSerializerDestroyAPIView.as_view(),name='TAGSSerializerDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerListCreateAPIView',TAGSSerializerListCreateAPIView.as_view(),name='TAGSSerializerListCreateAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveUpdateAPIView',TAGSSerializerRetrieveUpdateAPIView.as_view(),name='TAGSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveDestroyAPIView',TAGSSerializerRetrieveDestroyAPIView.as_view(),name='TAGSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveUpdateDestroyAPIView',TAGSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='TAGSSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerAPIView',ASSIGNATIONSerializerAPIView.as_view(),name='ASSIGNATIONSerializerAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerGenericAPIView',ASSIGNATIONSerializerGenericAPIView.as_view(),name='ASSIGNATIONSerializerGenericAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerListAPIView',ASSIGNATIONSerializerListAPIView.as_view(),name='ASSIGNATIONSerializerListAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveAPIView',ASSIGNATIONSerializerRetrieveAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerCreateAPIView',ASSIGNATIONSerializerCreateAPIView.as_view(),name='ASSIGNATIONSerializerCreateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerUpdateAPIView',ASSIGNATIONSerializerUpdateAPIView.as_view(),name='ASSIGNATIONSerializerUpdateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerDestroyAPIView',ASSIGNATIONSerializerDestroyAPIView.as_view(),name='ASSIGNATIONSerializerDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerListCreateAPIView',ASSIGNATIONSerializerListCreateAPIView.as_view(),name='ASSIGNATIONSerializerListCreateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveUpdateAPIView',ASSIGNATIONSerializerRetrieveUpdateAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveDestroyAPIView',ASSIGNATIONSerializerRetrieveDestroyAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView',ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('PROFILESerializerAPIView',PROFILESerializerAPIView.as_view(),name='PROFILESerializerAPIView'),]

urlpatterns +=[path('PROFILESerializerGenericAPIView',PROFILESerializerGenericAPIView.as_view(),name='PROFILESerializerGenericAPIView'),]

urlpatterns +=[path('PROFILESerializerListAPIView',PROFILESerializerListAPIView.as_view(),name='PROFILESerializerListAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveAPIView',PROFILESerializerRetrieveAPIView.as_view(),name='PROFILESerializerRetrieveAPIView'),]

urlpatterns +=[path('PROFILESerializerCreateAPIView',PROFILESerializerCreateAPIView.as_view(),name='PROFILESerializerCreateAPIView'),]

urlpatterns +=[path('PROFILESerializerUpdateAPIView',PROFILESerializerUpdateAPIView.as_view(),name='PROFILESerializerUpdateAPIView'),]

urlpatterns +=[path('PROFILESerializerDestroyAPIView',PROFILESerializerDestroyAPIView.as_view(),name='PROFILESerializerDestroyAPIView'),]

urlpatterns +=[path('PROFILESerializerListCreateAPIView',PROFILESerializerListCreateAPIView.as_view(),name='PROFILESerializerListCreateAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveUpdateAPIView',PROFILESerializerRetrieveUpdateAPIView.as_view(),name='PROFILESerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveDestroyAPIView',PROFILESerializerRetrieveDestroyAPIView.as_view(),name='PROFILESerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveUpdateDestroyAPIView',PROFILESerializerRetrieveUpdateDestroyAPIView.as_view(),name='PROFILESerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerAPIView',TASKSerializerAPIView.as_view(),name='TASKSerializerAPIView'),]

urlpatterns +=[path('TASKSerializerGenericAPIView',TASKSerializerGenericAPIView.as_view(),name='TASKSerializerGenericAPIView'),]

urlpatterns +=[path('TASKSerializerListAPIView',TASKSerializerListAPIView.as_view(),name='TASKSerializerListAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveAPIView',TASKSerializerRetrieveAPIView.as_view(),name='TASKSerializerRetrieveAPIView'),]

urlpatterns +=[path('TASKSerializerCreateAPIView',TASKSerializerCreateAPIView.as_view(),name='TASKSerializerCreateAPIView'),]

urlpatterns +=[path('TASKSerializerUpdateAPIView',TASKSerializerUpdateAPIView.as_view(),name='TASKSerializerUpdateAPIView'),]

urlpatterns +=[path('TASKSerializerDestroyAPIView',TASKSerializerDestroyAPIView.as_view(),name='TASKSerializerDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerListCreateAPIView',TASKSerializerListCreateAPIView.as_view(),name='TASKSerializerListCreateAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveUpdateAPIView',TASKSerializerRetrieveUpdateAPIView.as_view(),name='TASKSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveDestroyAPIView',TASKSerializerRetrieveDestroyAPIView.as_view(),name='TASKSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveUpdateDestroyAPIView',TASKSerializerRetrieveUpdateDestroyAPIView.as_view(),name='TASKSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerAPIView',TAGSSerializerAPIView.as_view(),name='TAGSSerializerAPIView'),]

urlpatterns +=[path('TAGSSerializerGenericAPIView',TAGSSerializerGenericAPIView.as_view(),name='TAGSSerializerGenericAPIView'),]

urlpatterns +=[path('TAGSSerializerListAPIView',TAGSSerializerListAPIView.as_view(),name='TAGSSerializerListAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveAPIView',TAGSSerializerRetrieveAPIView.as_view(),name='TAGSSerializerRetrieveAPIView'),]

urlpatterns +=[path('TAGSSerializerCreateAPIView',TAGSSerializerCreateAPIView.as_view(),name='TAGSSerializerCreateAPIView'),]

urlpatterns +=[path('TAGSSerializerUpdateAPIView',TAGSSerializerUpdateAPIView.as_view(),name='TAGSSerializerUpdateAPIView'),]

urlpatterns +=[path('TAGSSerializerDestroyAPIView',TAGSSerializerDestroyAPIView.as_view(),name='TAGSSerializerDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerListCreateAPIView',TAGSSerializerListCreateAPIView.as_view(),name='TAGSSerializerListCreateAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveUpdateAPIView',TAGSSerializerRetrieveUpdateAPIView.as_view(),name='TAGSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveDestroyAPIView',TAGSSerializerRetrieveDestroyAPIView.as_view(),name='TAGSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveUpdateDestroyAPIView',TAGSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='TAGSSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerAPIView',ASSIGNATIONSerializerAPIView.as_view(),name='ASSIGNATIONSerializerAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerGenericAPIView',ASSIGNATIONSerializerGenericAPIView.as_view(),name='ASSIGNATIONSerializerGenericAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerListAPIView',ASSIGNATIONSerializerListAPIView.as_view(),name='ASSIGNATIONSerializerListAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveAPIView',ASSIGNATIONSerializerRetrieveAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerCreateAPIView',ASSIGNATIONSerializerCreateAPIView.as_view(),name='ASSIGNATIONSerializerCreateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerUpdateAPIView',ASSIGNATIONSerializerUpdateAPIView.as_view(),name='ASSIGNATIONSerializerUpdateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerDestroyAPIView',ASSIGNATIONSerializerDestroyAPIView.as_view(),name='ASSIGNATIONSerializerDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerListCreateAPIView',ASSIGNATIONSerializerListCreateAPIView.as_view(),name='ASSIGNATIONSerializerListCreateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveUpdateAPIView',ASSIGNATIONSerializerRetrieveUpdateAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveDestroyAPIView',ASSIGNATIONSerializerRetrieveDestroyAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView',ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('PROFILESerializerAPIView',PROFILESerializerAPIView.as_view(),name='PROFILESerializerAPIView'),]

urlpatterns +=[path('PROFILESerializerGenericAPIView',PROFILESerializerGenericAPIView.as_view(),name='PROFILESerializerGenericAPIView'),]

urlpatterns +=[path('PROFILESerializerListAPIView',PROFILESerializerListAPIView.as_view(),name='PROFILESerializerListAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveAPIView',PROFILESerializerRetrieveAPIView.as_view(),name='PROFILESerializerRetrieveAPIView'),]

urlpatterns +=[path('PROFILESerializerCreateAPIView',PROFILESerializerCreateAPIView.as_view(),name='PROFILESerializerCreateAPIView'),]

urlpatterns +=[path('PROFILESerializerUpdateAPIView',PROFILESerializerUpdateAPIView.as_view(),name='PROFILESerializerUpdateAPIView'),]

urlpatterns +=[path('PROFILESerializerDestroyAPIView',PROFILESerializerDestroyAPIView.as_view(),name='PROFILESerializerDestroyAPIView'),]

urlpatterns +=[path('PROFILESerializerListCreateAPIView',PROFILESerializerListCreateAPIView.as_view(),name='PROFILESerializerListCreateAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveUpdateAPIView',PROFILESerializerRetrieveUpdateAPIView.as_view(),name='PROFILESerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveDestroyAPIView',PROFILESerializerRetrieveDestroyAPIView.as_view(),name='PROFILESerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveUpdateDestroyAPIView',PROFILESerializerRetrieveUpdateDestroyAPIView.as_view(),name='PROFILESerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerAPIView',TASKSerializerAPIView.as_view(),name='TASKSerializerAPIView'),]

urlpatterns +=[path('TASKSerializerGenericAPIView',TASKSerializerGenericAPIView.as_view(),name='TASKSerializerGenericAPIView'),]

urlpatterns +=[path('TASKSerializerListAPIView',TASKSerializerListAPIView.as_view(),name='TASKSerializerListAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveAPIView',TASKSerializerRetrieveAPIView.as_view(),name='TASKSerializerRetrieveAPIView'),]

urlpatterns +=[path('TASKSerializerCreateAPIView',TASKSerializerCreateAPIView.as_view(),name='TASKSerializerCreateAPIView'),]

urlpatterns +=[path('TASKSerializerUpdateAPIView',TASKSerializerUpdateAPIView.as_view(),name='TASKSerializerUpdateAPIView'),]

urlpatterns +=[path('TASKSerializerDestroyAPIView',TASKSerializerDestroyAPIView.as_view(),name='TASKSerializerDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerListCreateAPIView',TASKSerializerListCreateAPIView.as_view(),name='TASKSerializerListCreateAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveUpdateAPIView',TASKSerializerRetrieveUpdateAPIView.as_view(),name='TASKSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveDestroyAPIView',TASKSerializerRetrieveDestroyAPIView.as_view(),name='TASKSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveUpdateDestroyAPIView',TASKSerializerRetrieveUpdateDestroyAPIView.as_view(),name='TASKSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerAPIView',TAGSSerializerAPIView.as_view(),name='TAGSSerializerAPIView'),]

urlpatterns +=[path('TAGSSerializerGenericAPIView',TAGSSerializerGenericAPIView.as_view(),name='TAGSSerializerGenericAPIView'),]

urlpatterns +=[path('TAGSSerializerListAPIView',TAGSSerializerListAPIView.as_view(),name='TAGSSerializerListAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveAPIView',TAGSSerializerRetrieveAPIView.as_view(),name='TAGSSerializerRetrieveAPIView'),]

urlpatterns +=[path('TAGSSerializerCreateAPIView',TAGSSerializerCreateAPIView.as_view(),name='TAGSSerializerCreateAPIView'),]

urlpatterns +=[path('TAGSSerializerUpdateAPIView',TAGSSerializerUpdateAPIView.as_view(),name='TAGSSerializerUpdateAPIView'),]

urlpatterns +=[path('TAGSSerializerDestroyAPIView',TAGSSerializerDestroyAPIView.as_view(),name='TAGSSerializerDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerListCreateAPIView',TAGSSerializerListCreateAPIView.as_view(),name='TAGSSerializerListCreateAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveUpdateAPIView',TAGSSerializerRetrieveUpdateAPIView.as_view(),name='TAGSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveDestroyAPIView',TAGSSerializerRetrieveDestroyAPIView.as_view(),name='TAGSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveUpdateDestroyAPIView',TAGSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='TAGSSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerAPIView',ASSIGNATIONSerializerAPIView.as_view(),name='ASSIGNATIONSerializerAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerGenericAPIView',ASSIGNATIONSerializerGenericAPIView.as_view(),name='ASSIGNATIONSerializerGenericAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerListAPIView',ASSIGNATIONSerializerListAPIView.as_view(),name='ASSIGNATIONSerializerListAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveAPIView',ASSIGNATIONSerializerRetrieveAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerCreateAPIView',ASSIGNATIONSerializerCreateAPIView.as_view(),name='ASSIGNATIONSerializerCreateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerUpdateAPIView',ASSIGNATIONSerializerUpdateAPIView.as_view(),name='ASSIGNATIONSerializerUpdateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerDestroyAPIView',ASSIGNATIONSerializerDestroyAPIView.as_view(),name='ASSIGNATIONSerializerDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerListCreateAPIView',ASSIGNATIONSerializerListCreateAPIView.as_view(),name='ASSIGNATIONSerializerListCreateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveUpdateAPIView',ASSIGNATIONSerializerRetrieveUpdateAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveDestroyAPIView',ASSIGNATIONSerializerRetrieveDestroyAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView',ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('PROFILESerializerAPIView',PROFILESerializerAPIView.as_view(),name='PROFILESerializerAPIView'),]

urlpatterns +=[path('PROFILESerializerGenericAPIView',PROFILESerializerGenericAPIView.as_view(),name='PROFILESerializerGenericAPIView'),]

urlpatterns +=[path('PROFILESerializerListAPIView',PROFILESerializerListAPIView.as_view(),name='PROFILESerializerListAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveAPIView',PROFILESerializerRetrieveAPIView.as_view(),name='PROFILESerializerRetrieveAPIView'),]

urlpatterns +=[path('PROFILESerializerCreateAPIView',PROFILESerializerCreateAPIView.as_view(),name='PROFILESerializerCreateAPIView'),]

urlpatterns +=[path('PROFILESerializerUpdateAPIView',PROFILESerializerUpdateAPIView.as_view(),name='PROFILESerializerUpdateAPIView'),]

urlpatterns +=[path('PROFILESerializerDestroyAPIView',PROFILESerializerDestroyAPIView.as_view(),name='PROFILESerializerDestroyAPIView'),]

urlpatterns +=[path('PROFILESerializerListCreateAPIView',PROFILESerializerListCreateAPIView.as_view(),name='PROFILESerializerListCreateAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveUpdateAPIView',PROFILESerializerRetrieveUpdateAPIView.as_view(),name='PROFILESerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveDestroyAPIView',PROFILESerializerRetrieveDestroyAPIView.as_view(),name='PROFILESerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('PROFILESerializerRetrieveUpdateDestroyAPIView',PROFILESerializerRetrieveUpdateDestroyAPIView.as_view(),name='PROFILESerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerAPIView',TASKSerializerAPIView.as_view(),name='TASKSerializerAPIView'),]

urlpatterns +=[path('TASKSerializerGenericAPIView',TASKSerializerGenericAPIView.as_view(),name='TASKSerializerGenericAPIView'),]

urlpatterns +=[path('TASKSerializerListAPIView',TASKSerializerListAPIView.as_view(),name='TASKSerializerListAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveAPIView',TASKSerializerRetrieveAPIView.as_view(),name='TASKSerializerRetrieveAPIView'),]

urlpatterns +=[path('TASKSerializerCreateAPIView',TASKSerializerCreateAPIView.as_view(),name='TASKSerializerCreateAPIView'),]

urlpatterns +=[path('TASKSerializerUpdateAPIView',TASKSerializerUpdateAPIView.as_view(),name='TASKSerializerUpdateAPIView'),]

urlpatterns +=[path('TASKSerializerDestroyAPIView',TASKSerializerDestroyAPIView.as_view(),name='TASKSerializerDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerListCreateAPIView',TASKSerializerListCreateAPIView.as_view(),name='TASKSerializerListCreateAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveUpdateAPIView',TASKSerializerRetrieveUpdateAPIView.as_view(),name='TASKSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveDestroyAPIView',TASKSerializerRetrieveDestroyAPIView.as_view(),name='TASKSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('TASKSerializerRetrieveUpdateDestroyAPIView',TASKSerializerRetrieveUpdateDestroyAPIView.as_view(),name='TASKSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerAPIView',TAGSSerializerAPIView.as_view(),name='TAGSSerializerAPIView'),]

urlpatterns +=[path('TAGSSerializerGenericAPIView',TAGSSerializerGenericAPIView.as_view(),name='TAGSSerializerGenericAPIView'),]

urlpatterns +=[path('TAGSSerializerListAPIView',TAGSSerializerListAPIView.as_view(),name='TAGSSerializerListAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveAPIView',TAGSSerializerRetrieveAPIView.as_view(),name='TAGSSerializerRetrieveAPIView'),]

urlpatterns +=[path('TAGSSerializerCreateAPIView',TAGSSerializerCreateAPIView.as_view(),name='TAGSSerializerCreateAPIView'),]

urlpatterns +=[path('TAGSSerializerUpdateAPIView',TAGSSerializerUpdateAPIView.as_view(),name='TAGSSerializerUpdateAPIView'),]

urlpatterns +=[path('TAGSSerializerDestroyAPIView',TAGSSerializerDestroyAPIView.as_view(),name='TAGSSerializerDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerListCreateAPIView',TAGSSerializerListCreateAPIView.as_view(),name='TAGSSerializerListCreateAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveUpdateAPIView',TAGSSerializerRetrieveUpdateAPIView.as_view(),name='TAGSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveDestroyAPIView',TAGSSerializerRetrieveDestroyAPIView.as_view(),name='TAGSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('TAGSSerializerRetrieveUpdateDestroyAPIView',TAGSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='TAGSSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerAPIView',ASSIGNATIONSerializerAPIView.as_view(),name='ASSIGNATIONSerializerAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerGenericAPIView',ASSIGNATIONSerializerGenericAPIView.as_view(),name='ASSIGNATIONSerializerGenericAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerListAPIView',ASSIGNATIONSerializerListAPIView.as_view(),name='ASSIGNATIONSerializerListAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveAPIView',ASSIGNATIONSerializerRetrieveAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerCreateAPIView',ASSIGNATIONSerializerCreateAPIView.as_view(),name='ASSIGNATIONSerializerCreateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerUpdateAPIView',ASSIGNATIONSerializerUpdateAPIView.as_view(),name='ASSIGNATIONSerializerUpdateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerDestroyAPIView',ASSIGNATIONSerializerDestroyAPIView.as_view(),name='ASSIGNATIONSerializerDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerListCreateAPIView',ASSIGNATIONSerializerListCreateAPIView.as_view(),name='ASSIGNATIONSerializerListCreateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveUpdateAPIView',ASSIGNATIONSerializerRetrieveUpdateAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveDestroyAPIView',ASSIGNATIONSerializerRetrieveDestroyAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView',ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView.as_view(),name='ASSIGNATIONSerializerRetrieveUpdateDestroyAPIView'),]
