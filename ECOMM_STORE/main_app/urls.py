
from django.contrib import admin
from django.urls import path

from main_app.views import *
urlpatterns=[]
urlpatterns +=[path('',Index.as_view(),name='Index'),]
urlpatterns +=[path('PRODUCTS_CREATEVIEW',PRODUCTS_CREATEVIEW.as_view(),name='PRODUCTS_CREATEVIEW'),]

urlpatterns +=[path('CARTS_CREATEVIEW',CARTS_CREATEVIEW.as_view(),name='CARTS_CREATEVIEW'),]

urlpatterns +=[path('SURVEY_CREATEVIEW',SURVEY_CREATEVIEW.as_view(),name='SURVEY_CREATEVIEW'),]

urlpatterns +=[path('PRODUCTS_LISTVIEW',PRODUCTS_LISTVIEW.as_view(),name='PRODUCTS_LISTVIEW'),]

urlpatterns +=[path('CARTS_LISTVIEW',CARTS_LISTVIEW.as_view(),name='CARTS_LISTVIEW'),]

urlpatterns +=[path('SURVEY_LISTVIEW',SURVEY_LISTVIEW.as_view(),name='SURVEY_LISTVIEW'),]

urlpatterns +=[path('PRODUCTS_UPDATEVIEW/<int:pk>',PRODUCTS_UPDATEVIEW.as_view(),name='PRODUCTS_UPDATEVIEW'),]

urlpatterns +=[path('CARTS_UPDATEVIEW/<int:pk>',CARTS_UPDATEVIEW.as_view(),name='CARTS_UPDATEVIEW'),]

urlpatterns +=[path('SURVEY_UPDATEVIEW/<int:pk>',SURVEY_UPDATEVIEW.as_view(),name='SURVEY_UPDATEVIEW'),]

urlpatterns +=[path('PRODUCTS_DETAILVIEW/<int:pk>',PRODUCTS_DETAILVIEW.as_view(),name='PRODUCTS_DETAILVIEW'),]

urlpatterns +=[path('CARTS_DETAILVIEW/<int:pk>',CARTS_DETAILVIEW.as_view(),name='CARTS_DETAILVIEW'),]

urlpatterns +=[path('SURVEY_DETAILVIEW/<int:pk>',SURVEY_DETAILVIEW.as_view(),name='SURVEY_DETAILVIEW'),]

urlpatterns +=[path('PRODUCTS_DELETEVIEW/<int:pk>',PRODUCTS_DELETEVIEW.as_view(),name='PRODUCTS_DELETEVIEW'),]

urlpatterns +=[path('CARTS_DELETEVIEW/<int:pk>',CARTS_DELETEVIEW.as_view(),name='CARTS_DELETEVIEW'),]

urlpatterns +=[path('SURVEY_DELETEVIEW/<int:pk>',SURVEY_DELETEVIEW.as_view(),name='SURVEY_DELETEVIEW'),]

urlpatterns +=[path('PRODUCTSSerializerAPIView',PRODUCTSSerializerAPIView.as_view(),name='PRODUCTSSerializerAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerGenericAPIView',PRODUCTSSerializerGenericAPIView.as_view(),name='PRODUCTSSerializerGenericAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerListAPIView',PRODUCTSSerializerListAPIView.as_view(),name='PRODUCTSSerializerListAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveAPIView',PRODUCTSSerializerRetrieveAPIView.as_view(),name='PRODUCTSSerializerRetrieveAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerCreateAPIView',PRODUCTSSerializerCreateAPIView.as_view(),name='PRODUCTSSerializerCreateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerUpdateAPIView',PRODUCTSSerializerUpdateAPIView.as_view(),name='PRODUCTSSerializerUpdateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerDestroyAPIView',PRODUCTSSerializerDestroyAPIView.as_view(),name='PRODUCTSSerializerDestroyAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerListCreateAPIView',PRODUCTSSerializerListCreateAPIView.as_view(),name='PRODUCTSSerializerListCreateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveUpdateAPIView',PRODUCTSSerializerRetrieveUpdateAPIView.as_view(),name='PRODUCTSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveDestroyAPIView',PRODUCTSSerializerRetrieveDestroyAPIView.as_view(),name='PRODUCTSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveUpdateDestroyAPIView',PRODUCTSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='PRODUCTSSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('CARTSSerializerAPIView',CARTSSerializerAPIView.as_view(),name='CARTSSerializerAPIView'),]

urlpatterns +=[path('CARTSSerializerGenericAPIView',CARTSSerializerGenericAPIView.as_view(),name='CARTSSerializerGenericAPIView'),]

urlpatterns +=[path('CARTSSerializerListAPIView',CARTSSerializerListAPIView.as_view(),name='CARTSSerializerListAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveAPIView',CARTSSerializerRetrieveAPIView.as_view(),name='CARTSSerializerRetrieveAPIView'),]

urlpatterns +=[path('CARTSSerializerCreateAPIView',CARTSSerializerCreateAPIView.as_view(),name='CARTSSerializerCreateAPIView'),]

urlpatterns +=[path('CARTSSerializerUpdateAPIView',CARTSSerializerUpdateAPIView.as_view(),name='CARTSSerializerUpdateAPIView'),]

urlpatterns +=[path('CARTSSerializerDestroyAPIView',CARTSSerializerDestroyAPIView.as_view(),name='CARTSSerializerDestroyAPIView'),]

urlpatterns +=[path('CARTSSerializerListCreateAPIView',CARTSSerializerListCreateAPIView.as_view(),name='CARTSSerializerListCreateAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveUpdateAPIView',CARTSSerializerRetrieveUpdateAPIView.as_view(),name='CARTSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveDestroyAPIView',CARTSSerializerRetrieveDestroyAPIView.as_view(),name='CARTSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveUpdateDestroyAPIView',CARTSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='CARTSSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('SURVEYSerializerAPIView',SURVEYSerializerAPIView.as_view(),name='SURVEYSerializerAPIView'),]

urlpatterns +=[path('SURVEYSerializerGenericAPIView',SURVEYSerializerGenericAPIView.as_view(),name='SURVEYSerializerGenericAPIView'),]

urlpatterns +=[path('SURVEYSerializerListAPIView',SURVEYSerializerListAPIView.as_view(),name='SURVEYSerializerListAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveAPIView',SURVEYSerializerRetrieveAPIView.as_view(),name='SURVEYSerializerRetrieveAPIView'),]

urlpatterns +=[path('SURVEYSerializerCreateAPIView',SURVEYSerializerCreateAPIView.as_view(),name='SURVEYSerializerCreateAPIView'),]

urlpatterns +=[path('SURVEYSerializerUpdateAPIView',SURVEYSerializerUpdateAPIView.as_view(),name='SURVEYSerializerUpdateAPIView'),]

urlpatterns +=[path('SURVEYSerializerDestroyAPIView',SURVEYSerializerDestroyAPIView.as_view(),name='SURVEYSerializerDestroyAPIView'),]

urlpatterns +=[path('SURVEYSerializerListCreateAPIView',SURVEYSerializerListCreateAPIView.as_view(),name='SURVEYSerializerListCreateAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveUpdateAPIView',SURVEYSerializerRetrieveUpdateAPIView.as_view(),name='SURVEYSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveDestroyAPIView',SURVEYSerializerRetrieveDestroyAPIView.as_view(),name='SURVEYSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveUpdateDestroyAPIView',SURVEYSerializerRetrieveUpdateDestroyAPIView.as_view(),name='SURVEYSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerAPIView',PRODUCTSSerializerAPIView.as_view(),name='PRODUCTSSerializerAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerGenericAPIView',PRODUCTSSerializerGenericAPIView.as_view(),name='PRODUCTSSerializerGenericAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerListAPIView',PRODUCTSSerializerListAPIView.as_view(),name='PRODUCTSSerializerListAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveAPIView',PRODUCTSSerializerRetrieveAPIView.as_view(),name='PRODUCTSSerializerRetrieveAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerCreateAPIView',PRODUCTSSerializerCreateAPIView.as_view(),name='PRODUCTSSerializerCreateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerUpdateAPIView',PRODUCTSSerializerUpdateAPIView.as_view(),name='PRODUCTSSerializerUpdateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerDestroyAPIView',PRODUCTSSerializerDestroyAPIView.as_view(),name='PRODUCTSSerializerDestroyAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerListCreateAPIView',PRODUCTSSerializerListCreateAPIView.as_view(),name='PRODUCTSSerializerListCreateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveUpdateAPIView',PRODUCTSSerializerRetrieveUpdateAPIView.as_view(),name='PRODUCTSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveDestroyAPIView',PRODUCTSSerializerRetrieveDestroyAPIView.as_view(),name='PRODUCTSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveUpdateDestroyAPIView',PRODUCTSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='PRODUCTSSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('CARTSSerializerAPIView',CARTSSerializerAPIView.as_view(),name='CARTSSerializerAPIView'),]

urlpatterns +=[path('CARTSSerializerGenericAPIView',CARTSSerializerGenericAPIView.as_view(),name='CARTSSerializerGenericAPIView'),]

urlpatterns +=[path('CARTSSerializerListAPIView',CARTSSerializerListAPIView.as_view(),name='CARTSSerializerListAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveAPIView',CARTSSerializerRetrieveAPIView.as_view(),name='CARTSSerializerRetrieveAPIView'),]

urlpatterns +=[path('CARTSSerializerCreateAPIView',CARTSSerializerCreateAPIView.as_view(),name='CARTSSerializerCreateAPIView'),]

urlpatterns +=[path('CARTSSerializerUpdateAPIView',CARTSSerializerUpdateAPIView.as_view(),name='CARTSSerializerUpdateAPIView'),]

urlpatterns +=[path('CARTSSerializerDestroyAPIView',CARTSSerializerDestroyAPIView.as_view(),name='CARTSSerializerDestroyAPIView'),]

urlpatterns +=[path('CARTSSerializerListCreateAPIView',CARTSSerializerListCreateAPIView.as_view(),name='CARTSSerializerListCreateAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveUpdateAPIView',CARTSSerializerRetrieveUpdateAPIView.as_view(),name='CARTSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveDestroyAPIView',CARTSSerializerRetrieveDestroyAPIView.as_view(),name='CARTSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveUpdateDestroyAPIView',CARTSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='CARTSSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('SURVEYSerializerAPIView',SURVEYSerializerAPIView.as_view(),name='SURVEYSerializerAPIView'),]

urlpatterns +=[path('SURVEYSerializerGenericAPIView',SURVEYSerializerGenericAPIView.as_view(),name='SURVEYSerializerGenericAPIView'),]

urlpatterns +=[path('SURVEYSerializerListAPIView',SURVEYSerializerListAPIView.as_view(),name='SURVEYSerializerListAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveAPIView',SURVEYSerializerRetrieveAPIView.as_view(),name='SURVEYSerializerRetrieveAPIView'),]

urlpatterns +=[path('SURVEYSerializerCreateAPIView',SURVEYSerializerCreateAPIView.as_view(),name='SURVEYSerializerCreateAPIView'),]

urlpatterns +=[path('SURVEYSerializerUpdateAPIView',SURVEYSerializerUpdateAPIView.as_view(),name='SURVEYSerializerUpdateAPIView'),]

urlpatterns +=[path('SURVEYSerializerDestroyAPIView',SURVEYSerializerDestroyAPIView.as_view(),name='SURVEYSerializerDestroyAPIView'),]

urlpatterns +=[path('SURVEYSerializerListCreateAPIView',SURVEYSerializerListCreateAPIView.as_view(),name='SURVEYSerializerListCreateAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveUpdateAPIView',SURVEYSerializerRetrieveUpdateAPIView.as_view(),name='SURVEYSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveDestroyAPIView',SURVEYSerializerRetrieveDestroyAPIView.as_view(),name='SURVEYSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveUpdateDestroyAPIView',SURVEYSerializerRetrieveUpdateDestroyAPIView.as_view(),name='SURVEYSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerAPIView',PRODUCTSSerializerAPIView.as_view(),name='PRODUCTSSerializerAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerGenericAPIView',PRODUCTSSerializerGenericAPIView.as_view(),name='PRODUCTSSerializerGenericAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerListAPIView',PRODUCTSSerializerListAPIView.as_view(),name='PRODUCTSSerializerListAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveAPIView',PRODUCTSSerializerRetrieveAPIView.as_view(),name='PRODUCTSSerializerRetrieveAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerCreateAPIView',PRODUCTSSerializerCreateAPIView.as_view(),name='PRODUCTSSerializerCreateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerUpdateAPIView',PRODUCTSSerializerUpdateAPIView.as_view(),name='PRODUCTSSerializerUpdateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerDestroyAPIView',PRODUCTSSerializerDestroyAPIView.as_view(),name='PRODUCTSSerializerDestroyAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerListCreateAPIView',PRODUCTSSerializerListCreateAPIView.as_view(),name='PRODUCTSSerializerListCreateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveUpdateAPIView',PRODUCTSSerializerRetrieveUpdateAPIView.as_view(),name='PRODUCTSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveDestroyAPIView',PRODUCTSSerializerRetrieveDestroyAPIView.as_view(),name='PRODUCTSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('PRODUCTSSerializerRetrieveUpdateDestroyAPIView',PRODUCTSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='PRODUCTSSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('CARTSSerializerAPIView',CARTSSerializerAPIView.as_view(),name='CARTSSerializerAPIView'),]

urlpatterns +=[path('CARTSSerializerGenericAPIView',CARTSSerializerGenericAPIView.as_view(),name='CARTSSerializerGenericAPIView'),]

urlpatterns +=[path('CARTSSerializerListAPIView',CARTSSerializerListAPIView.as_view(),name='CARTSSerializerListAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveAPIView',CARTSSerializerRetrieveAPIView.as_view(),name='CARTSSerializerRetrieveAPIView'),]

urlpatterns +=[path('CARTSSerializerCreateAPIView',CARTSSerializerCreateAPIView.as_view(),name='CARTSSerializerCreateAPIView'),]

urlpatterns +=[path('CARTSSerializerUpdateAPIView',CARTSSerializerUpdateAPIView.as_view(),name='CARTSSerializerUpdateAPIView'),]

urlpatterns +=[path('CARTSSerializerDestroyAPIView',CARTSSerializerDestroyAPIView.as_view(),name='CARTSSerializerDestroyAPIView'),]

urlpatterns +=[path('CARTSSerializerListCreateAPIView',CARTSSerializerListCreateAPIView.as_view(),name='CARTSSerializerListCreateAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveUpdateAPIView',CARTSSerializerRetrieveUpdateAPIView.as_view(),name='CARTSSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveDestroyAPIView',CARTSSerializerRetrieveDestroyAPIView.as_view(),name='CARTSSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('CARTSSerializerRetrieveUpdateDestroyAPIView',CARTSSerializerRetrieveUpdateDestroyAPIView.as_view(),name='CARTSSerializerRetrieveUpdateDestroyAPIView'),]

urlpatterns +=[path('SURVEYSerializerAPIView',SURVEYSerializerAPIView.as_view(),name='SURVEYSerializerAPIView'),]

urlpatterns +=[path('SURVEYSerializerGenericAPIView',SURVEYSerializerGenericAPIView.as_view(),name='SURVEYSerializerGenericAPIView'),]

urlpatterns +=[path('SURVEYSerializerListAPIView',SURVEYSerializerListAPIView.as_view(),name='SURVEYSerializerListAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveAPIView',SURVEYSerializerRetrieveAPIView.as_view(),name='SURVEYSerializerRetrieveAPIView'),]

urlpatterns +=[path('SURVEYSerializerCreateAPIView',SURVEYSerializerCreateAPIView.as_view(),name='SURVEYSerializerCreateAPIView'),]

urlpatterns +=[path('SURVEYSerializerUpdateAPIView',SURVEYSerializerUpdateAPIView.as_view(),name='SURVEYSerializerUpdateAPIView'),]

urlpatterns +=[path('SURVEYSerializerDestroyAPIView',SURVEYSerializerDestroyAPIView.as_view(),name='SURVEYSerializerDestroyAPIView'),]

urlpatterns +=[path('SURVEYSerializerListCreateAPIView',SURVEYSerializerListCreateAPIView.as_view(),name='SURVEYSerializerListCreateAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveUpdateAPIView',SURVEYSerializerRetrieveUpdateAPIView.as_view(),name='SURVEYSerializerRetrieveUpdateAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveDestroyAPIView',SURVEYSerializerRetrieveDestroyAPIView.as_view(),name='SURVEYSerializerRetrieveDestroyAPIView'),]

urlpatterns +=[path('SURVEYSerializerRetrieveUpdateDestroyAPIView',SURVEYSerializerRetrieveUpdateDestroyAPIView.as_view(),name='SURVEYSerializerRetrieveUpdateDestroyAPIView'),]
