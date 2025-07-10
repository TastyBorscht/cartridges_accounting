from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import (
    ListView,
    UpdateView, DeleteView)

from .forms import (
    CartridgeCreateForm,
    CartridgeUpdateForm,
    )
from .models import Cartridge

class CartridgeListView(ListView):
    model = Cartridge
    template_name = 'cartridges/main.html'
    context_object_name = 'cartridges'

    def get_queryset(self):
        return Cartridge.objects.only(
            'name', 'device_name', 'acceptance_date', 'inventory_number'
        )


# class CartridgeManageView(View):
#     template_name = 'cartridge_form.html'
#
#     def get(self, request, pk=None):
#         if pk:
#             obj = get_object_or_404(Cartridge, pk=pk)
#             form = CartridgeCreateForm(instance=obj)
#         else:
#             form = CartridgeCreateForm()
#         cartridges = Cartridge.objects.all()
#         return render(request, self.template_name, {
#             'form': form,
#             'cartridges': cartridges,
#             'pk': pk,
#         })
#
#     def post(self, request, pk=None):
#         if 'delete' in request.POST:
#             obj = get_object_or_404(Cartridge, pk=pk)
#             obj.delete()
#             return redirect('cartridge_manage')
#         else:
#             if pk:
#                 obj = get_object_or_404(Cartridge, pk=pk)
#                 form = CartridgeCreateForm(request.POST, instance=obj)
#             else:
#                 form = CartridgeCreateForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('cartridge_manage')
#         cartridges = Cartridge.objects.all()
#         return render(request, self.template_name, {
#             'form': form,
#             'cartridges': cartridges,
#             'pk': pk,
#         })

class CartridgeManageView(View):
    template_name = 'cartridges/cartridge_form.html'

    def get(self, request):
        form = CartridgeCreateForm()
        cartridges = Cartridge.objects.all()
        return render(request, self.template_name, {
            'form': form,
            'cartridges': cartridges,
        })

    def post(self, request):
        form = CartridgeCreateForm(request.POST)
        if form.is_valid():
            cartridge = form.save(commit=False)
            cartridge.added_by = request.user
            cartridge.save()
            return redirect('cartridges:cartridge_manage')
        cartridges = Cartridge.objects.all()
        return render(request, self.template_name, {
            'form': form,
            'cartridges': cartridges,
        })

class CartridgeUpdateView(UpdateView):
    model = Cartridge
    form_class = CartridgeUpdateForm
    template_name = 'cartridges/cartridge_update.html'
    success_url = '/'

class CartridgeDeleteView(DeleteView):
    model = Cartridge
    success_url = '/'

