from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import CartridgeForm
from .models import Cartridge

class CartridgeListView(ListView):
    model = Cartridge
    template_name = 'main.html'
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
#             form = CartridgeForm(instance=obj)
#         else:
#             form = CartridgeForm()
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
#                 form = CartridgeForm(request.POST, instance=obj)
#             else:
#                 form = CartridgeForm(request.POST)
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
    template_name = 'cartridge_form.html'

    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(Cartridge, pk=pk)
            form = CartridgeForm(instance=obj)
        else:
            form = CartridgeForm()
        cartridges = Cartridge.objects.all()
        return render(request, self.template_name, {
            'form': form,
            'cartridges': cartridges,
            'pk': pk,
        })

    def post(self, request, pk=None):
        if 'delete' in request.POST:
            obj = get_object_or_404(Cartridge, pk=pk)
            obj.delete()
            return redirect('cartridges:cartridge_manage')
        else:
            if pk:
                obj = get_object_or_404(Cartridge, pk=pk)
                form = CartridgeForm(request.POST, instance=obj)
            else:
                form = CartridgeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('cartridges:cartridge_manage')
        cartridges = Cartridge.objects.all()
        return render(request, self.template_name, {
            'form': form,
            'cartridges': cartridges,
            'pk': pk,
        })

