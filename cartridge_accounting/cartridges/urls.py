from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cartridges'

urlpatterns = [
    path('', views.CartridgeListView.as_view(), name='cartridges_list',),
    path('<int:pk>/update/', views.CartridgeUpdateView.as_view(), name='cartridges_update'),
    path('cartridge_manage/', views.CartridgeManageView.as_view(), name='cartridge_manage'),
    path('cartridge_manage/<int:pk>/', views.CartridgeManageView.as_view(), name='cartridge_edit'),
] + static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
