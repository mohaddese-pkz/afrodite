from django.urls import path
from . import api_view


urlpatterns = [
    path('create/', api_view.SiteSettingCreate.as_view(), name='sitesetting_create'),
    path('edit/<int:id>', api_view.SiteSettingUpdate.as_view(), name='SiteSettingUpdate'),
    path('list/', api_view.SiteSettingList.as_view(), name='sitesetting_list'),
]