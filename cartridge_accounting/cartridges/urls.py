from django.urls import path, include

from cartridges.views import CartridgeListView, CartridgeManageView

app_name = 'cartridges'

urlpatterns = [
    path('', CartridgeListView.as_view(), name='cartridges_list',),
    path('cartridge_manage', CartridgeManageView.as_view(), name='cartridge_manage')
]
