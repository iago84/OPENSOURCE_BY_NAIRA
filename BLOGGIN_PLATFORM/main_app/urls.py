
from django.contrib import admin
from django.urls import path

from main_app.views import *
urlpatterns=[]
urlpatterns +=[path('',Index.as_view(),name='Index'),]
urlpatterns +=[path('PROFILE_CREATEVIEW',PROFILE_CREATEVIEW.as_view(),name='PROFILE_CREATEVIEW'),]

urlpatterns +=[path('PUBLICATION_CREATEVIEW',PUBLICATION_CREATEVIEW.as_view(),name='PUBLICATION_CREATEVIEW'),]

urlpatterns +=[path('COMMENTS_CREATEVIEW',COMMENTS_CREATEVIEW.as_view(),name='COMMENTS_CREATEVIEW'),]

urlpatterns +=[path('TAGS_CREATEVIEW',TAGS_CREATEVIEW.as_view(),name='TAGS_CREATEVIEW'),]

urlpatterns +=[path('PROFILE_LISTVIEW',PROFILE_LISTVIEW.as_view(),name='PROFILE_LISTVIEW'),]

urlpatterns +=[path('PUBLICATION_LISTVIEW',PUBLICATION_LISTVIEW.as_view(),name='PUBLICATION_LISTVIEW'),]

urlpatterns +=[path('COMMENTS_LISTVIEW',COMMENTS_LISTVIEW.as_view(),name='COMMENTS_LISTVIEW'),]

urlpatterns +=[path('TAGS_LISTVIEW',TAGS_LISTVIEW.as_view(),name='TAGS_LISTVIEW'),]

urlpatterns +=[path('PROFILE_UPDATEVIEW/<int:pk>',PROFILE_UPDATEVIEW.as_view(),name='PROFILE_UPDATEVIEW'),]

urlpatterns +=[path('PUBLICATION_UPDATEVIEW/<int:pk>',PUBLICATION_UPDATEVIEW.as_view(),name='PUBLICATION_UPDATEVIEW'),]

urlpatterns +=[path('COMMENTS_UPDATEVIEW/<int:pk>',COMMENTS_UPDATEVIEW.as_view(),name='COMMENTS_UPDATEVIEW'),]

urlpatterns +=[path('TAGS_UPDATEVIEW/<int:pk>',TAGS_UPDATEVIEW.as_view(),name='TAGS_UPDATEVIEW'),]

urlpatterns +=[path('PROFILE_DETAILVIEW/<int:pk>',PROFILE_DETAILVIEW.as_view(),name='PROFILE_DETAILVIEW'),]

urlpatterns +=[path('PUBLICATION_DETAILVIEW/<int:pk>',PUBLICATION_DETAILVIEW.as_view(),name='PUBLICATION_DETAILVIEW'),]

urlpatterns +=[path('COMMENTS_DETAILVIEW/<int:pk>',COMMENTS_DETAILVIEW.as_view(),name='COMMENTS_DETAILVIEW'),]

urlpatterns +=[path('TAGS_DETAILVIEW/<int:pk>',TAGS_DETAILVIEW.as_view(),name='TAGS_DETAILVIEW'),]

urlpatterns +=[path('PROFILE_DELETEVIEW/<int:pk>',PROFILE_DELETEVIEW.as_view(),name='PROFILE_DELETEVIEW'),]

urlpatterns +=[path('PUBLICATION_DELETEVIEW/<int:pk>',PUBLICATION_DELETEVIEW.as_view(),name='PUBLICATION_DELETEVIEW'),]

urlpatterns +=[path('COMMENTS_DELETEVIEW/<int:pk>',COMMENTS_DELETEVIEW.as_view(),name='COMMENTS_DELETEVIEW'),]

urlpatterns +=[path('TAGS_DELETEVIEW/<int:pk>',TAGS_DELETEVIEW.as_view(),name='TAGS_DELETEVIEW'),]

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

urlpatterns +=[path('PUBLICATIONSerializerAPIView',PUBLICATIONSerializerAPIView.as_view(),name='PUBLICATIONSerializerAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerGenericAPIView',PUBLICATIONSerializerGenericAPIView.as_view(),name='PUBLICATIONSerializerGenericAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerListAPIView',PUBLICATIONSerializerListAPIView.as_view(),name='PUBLICATIONSerializerListAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveAPIView',PUBLICATIONSerializerRetrieveAPIView.as_view(),name='PUBLICATIONSerializerRetrieveAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerCreateAPIView',PUBLICATIONSerializerCreateAPIView.as_view(),name='PUBLICATIONSerializerCreateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerUpdateAPIView',PUBLICATIONSerializerUpdateAPIView.as_view(),name='PUBLICATIONSerializerUpdateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerDestroyAPIView',PUBLICATIONSerializerDestroyAPIView.as_view(),name='PUBLICATIONSerializerDestroyAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerListCreateAPIView',PUBLICATIONSerializerListCreateAPIView.as_view(),name='PUBLICATIONSerializerListCreateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveUpdateAPIView',PUBLICATIONSerializerRetrieveUpdateAPIView.as_view(),name='PUBLICATIONSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveDestroyAPIView',PUBLICATIONSerializerRetrieveDestroyAPIView.as_view(),name='PUBLICATIONSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveUpdateDestroyAPIView',PUBLICATIONSerializerRetrieveUpdateDestroyAPIView.as_view(),name='PUBLICATIONSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerAPIView',COMMENTSSerializerAPIView.as_view(),name='COMMENTSSerializerAPIView'),]

urlpatterns +=[path('COMMENTSSerializerGenericAPIView',COMMENTSSerializerGenericAPIView.as_view(),name='COMMENTSSerializerGenericAPIView'),]

urlpatterns +=[path('COMMENTSSerializerListAPIView',COMMENTSSerializerListAPIView.as_view(),name='COMMENTSSerializerListAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveAPIView',COMMENTSSerializerRetrieveAPIView.as_view(),name='COMMENTSSerializerRetrieveAPIView'),]

urlpatterns +=[path('COMMENTSSerializerCreateAPIView',COMMENTSSerializerCreateAPIView.as_view(),name='COMMENTSSerializerCreateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerUpdateAPIView',COMMENTSSerializerUpdateAPIView.as_view(),name='COMMENTSSerializerUpdateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerDestroyAPIView',COMMENTSSerializerDestroyAPIView.as_view(),name='COMMENTSSerializerDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerListCreateAPIView',COMMENTSSerializerListCreateAPIView.as_view(),name='COMMENTSSerializerListCreateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveUpdateAPIView',COMMENTSSerializerRetrieveUpdateAPIView.as_view(),name='COMMENTSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveDestroyAPIView',COMMENTSSerializerRetrieveDestroyAPIView.as_view(),name='COMMENTSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveUpdateDestroyAPIView',COMMENTSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='COMMENTSSerializerRetrieveUpdateDestroyAPIView'),]

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

urlpatterns +=[path('PUBLICATIONSerializerAPIView',PUBLICATIONSerializerAPIView.as_view(),name='PUBLICATIONSerializerAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerGenericAPIView',PUBLICATIONSerializerGenericAPIView.as_view(),name='PUBLICATIONSerializerGenericAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerListAPIView',PUBLICATIONSerializerListAPIView.as_view(),name='PUBLICATIONSerializerListAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveAPIView',PUBLICATIONSerializerRetrieveAPIView.as_view(),name='PUBLICATIONSerializerRetrieveAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerCreateAPIView',PUBLICATIONSerializerCreateAPIView.as_view(),name='PUBLICATIONSerializerCreateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerUpdateAPIView',PUBLICATIONSerializerUpdateAPIView.as_view(),name='PUBLICATIONSerializerUpdateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerDestroyAPIView',PUBLICATIONSerializerDestroyAPIView.as_view(),name='PUBLICATIONSerializerDestroyAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerListCreateAPIView',PUBLICATIONSerializerListCreateAPIView.as_view(),name='PUBLICATIONSerializerListCreateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveUpdateAPIView',PUBLICATIONSerializerRetrieveUpdateAPIView.as_view(),name='PUBLICATIONSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveDestroyAPIView',PUBLICATIONSerializerRetrieveDestroyAPIView.as_view(),name='PUBLICATIONSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveUpdateDestroyAPIView',PUBLICATIONSerializerRetrieveUpdateDestroyAPIView.as_view(),name='PUBLICATIONSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerAPIView',COMMENTSSerializerAPIView.as_view(),name='COMMENTSSerializerAPIView'),]

urlpatterns +=[path('COMMENTSSerializerGenericAPIView',COMMENTSSerializerGenericAPIView.as_view(),name='COMMENTSSerializerGenericAPIView'),]

urlpatterns +=[path('COMMENTSSerializerListAPIView',COMMENTSSerializerListAPIView.as_view(),name='COMMENTSSerializerListAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveAPIView',COMMENTSSerializerRetrieveAPIView.as_view(),name='COMMENTSSerializerRetrieveAPIView'),]

urlpatterns +=[path('COMMENTSSerializerCreateAPIView',COMMENTSSerializerCreateAPIView.as_view(),name='COMMENTSSerializerCreateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerUpdateAPIView',COMMENTSSerializerUpdateAPIView.as_view(),name='COMMENTSSerializerUpdateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerDestroyAPIView',COMMENTSSerializerDestroyAPIView.as_view(),name='COMMENTSSerializerDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerListCreateAPIView',COMMENTSSerializerListCreateAPIView.as_view(),name='COMMENTSSerializerListCreateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveUpdateAPIView',COMMENTSSerializerRetrieveUpdateAPIView.as_view(),name='COMMENTSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveDestroyAPIView',COMMENTSSerializerRetrieveDestroyAPIView.as_view(),name='COMMENTSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveUpdateDestroyAPIView',COMMENTSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='COMMENTSSerializerRetrieveUpdateDestroyAPIView'),]

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

urlpatterns +=[path('PUBLICATIONSerializerAPIView',PUBLICATIONSerializerAPIView.as_view(),name='PUBLICATIONSerializerAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerGenericAPIView',PUBLICATIONSerializerGenericAPIView.as_view(),name='PUBLICATIONSerializerGenericAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerListAPIView',PUBLICATIONSerializerListAPIView.as_view(),name='PUBLICATIONSerializerListAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveAPIView',PUBLICATIONSerializerRetrieveAPIView.as_view(),name='PUBLICATIONSerializerRetrieveAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerCreateAPIView',PUBLICATIONSerializerCreateAPIView.as_view(),name='PUBLICATIONSerializerCreateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerUpdateAPIView',PUBLICATIONSerializerUpdateAPIView.as_view(),name='PUBLICATIONSerializerUpdateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerDestroyAPIView',PUBLICATIONSerializerDestroyAPIView.as_view(),name='PUBLICATIONSerializerDestroyAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerListCreateAPIView',PUBLICATIONSerializerListCreateAPIView.as_view(),name='PUBLICATIONSerializerListCreateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveUpdateAPIView',PUBLICATIONSerializerRetrieveUpdateAPIView.as_view(),name='PUBLICATIONSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveDestroyAPIView',PUBLICATIONSerializerRetrieveDestroyAPIView.as_view(),name='PUBLICATIONSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveUpdateDestroyAPIView',PUBLICATIONSerializerRetrieveUpdateDestroyAPIView.as_view(),name='PUBLICATIONSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerAPIView',COMMENTSSerializerAPIView.as_view(),name='COMMENTSSerializerAPIView'),]

urlpatterns +=[path('COMMENTSSerializerGenericAPIView',COMMENTSSerializerGenericAPIView.as_view(),name='COMMENTSSerializerGenericAPIView'),]

urlpatterns +=[path('COMMENTSSerializerListAPIView',COMMENTSSerializerListAPIView.as_view(),name='COMMENTSSerializerListAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveAPIView',COMMENTSSerializerRetrieveAPIView.as_view(),name='COMMENTSSerializerRetrieveAPIView'),]

urlpatterns +=[path('COMMENTSSerializerCreateAPIView',COMMENTSSerializerCreateAPIView.as_view(),name='COMMENTSSerializerCreateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerUpdateAPIView',COMMENTSSerializerUpdateAPIView.as_view(),name='COMMENTSSerializerUpdateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerDestroyAPIView',COMMENTSSerializerDestroyAPIView.as_view(),name='COMMENTSSerializerDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerListCreateAPIView',COMMENTSSerializerListCreateAPIView.as_view(),name='COMMENTSSerializerListCreateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveUpdateAPIView',COMMENTSSerializerRetrieveUpdateAPIView.as_view(),name='COMMENTSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveDestroyAPIView',COMMENTSSerializerRetrieveDestroyAPIView.as_view(),name='COMMENTSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveUpdateDestroyAPIView',COMMENTSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='COMMENTSSerializerRetrieveUpdateDestroyAPIView'),]

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

urlpatterns +=[path('PUBLICATIONSerializerAPIView',PUBLICATIONSerializerAPIView.as_view(),name='PUBLICATIONSerializerAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerGenericAPIView',PUBLICATIONSerializerGenericAPIView.as_view(),name='PUBLICATIONSerializerGenericAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerListAPIView',PUBLICATIONSerializerListAPIView.as_view(),name='PUBLICATIONSerializerListAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveAPIView',PUBLICATIONSerializerRetrieveAPIView.as_view(),name='PUBLICATIONSerializerRetrieveAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerCreateAPIView',PUBLICATIONSerializerCreateAPIView.as_view(),name='PUBLICATIONSerializerCreateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerUpdateAPIView',PUBLICATIONSerializerUpdateAPIView.as_view(),name='PUBLICATIONSerializerUpdateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerDestroyAPIView',PUBLICATIONSerializerDestroyAPIView.as_view(),name='PUBLICATIONSerializerDestroyAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerListCreateAPIView',PUBLICATIONSerializerListCreateAPIView.as_view(),name='PUBLICATIONSerializerListCreateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveUpdateAPIView',PUBLICATIONSerializerRetrieveUpdateAPIView.as_view(),name='PUBLICATIONSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveDestroyAPIView',PUBLICATIONSerializerRetrieveDestroyAPIView.as_view(),name='PUBLICATIONSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('PUBLICATIONSerializerRetrieveUpdateDestroyAPIView',PUBLICATIONSerializerRetrieveUpdateDestroyAPIView.as_view(),name='PUBLICATIONSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerAPIView',COMMENTSSerializerAPIView.as_view(),name='COMMENTSSerializerAPIView'),]

urlpatterns +=[path('COMMENTSSerializerGenericAPIView',COMMENTSSerializerGenericAPIView.as_view(),name='COMMENTSSerializerGenericAPIView'),]

urlpatterns +=[path('COMMENTSSerializerListAPIView',COMMENTSSerializerListAPIView.as_view(),name='COMMENTSSerializerListAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveAPIView',COMMENTSSerializerRetrieveAPIView.as_view(),name='COMMENTSSerializerRetrieveAPIView'),]

urlpatterns +=[path('COMMENTSSerializerCreateAPIView',COMMENTSSerializerCreateAPIView.as_view(),name='COMMENTSSerializerCreateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerUpdateAPIView',COMMENTSSerializerUpdateAPIView.as_view(),name='COMMENTSSerializerUpdateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerDestroyAPIView',COMMENTSSerializerDestroyAPIView.as_view(),name='COMMENTSSerializerDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerListCreateAPIView',COMMENTSSerializerListCreateAPIView.as_view(),name='COMMENTSSerializerListCreateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveUpdateAPIView',COMMENTSSerializerRetrieveUpdateAPIView.as_view(),name='COMMENTSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveDestroyAPIView',COMMENTSSerializerRetrieveDestroyAPIView.as_view(),name='COMMENTSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('COMMENTSSerializerRetrieveUpdateDestroyAPIView',COMMENTSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='COMMENTSSerializerRetrieveUpdateDestroyAPIView'),]

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
