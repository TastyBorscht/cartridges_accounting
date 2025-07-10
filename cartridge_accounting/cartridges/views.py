from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import (
    ListView,
    UpdateView)
from django.utils import timezone
from .forms import (
    CartridgeCreateForm,
    CartridgeUpdateForm,
)
from .models import Cartridge, CommissionedCartridge
from datetime import date

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

    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(Cartridge, pk=pk)
            form = CartridgeCreateForm(instance=obj)
        else:
            form = CartridgeCreateForm()
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
                form = CartridgeCreateForm(request.POST, instance=obj)
            else:
                form = CartridgeCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('cartridges:cartridge_manage')
        cartridges = Cartridge.objects.all()
        return render(request, self.template_name, {
            'form': form,
            'cartridges': cartridges,
            'pk': pk,
        })


def commission(request, pk):
    cartridge = get_object_or_404(Cartridge, pk=pk)  # Выносим получение объекта в начало функции

    if request.method == 'POST':
        location = request.POST.get('location', '').strip()

        if location:
            # Создаем запись в новой таблице
            CommissionedCartridge.objects.create(
                name=cartridge.name,
                device_name=cartridge.device_name,
                acceptance_date=cartridge.acceptance_date,
                decommissioning_date=cartridge.decommissioning_date or date.today(),
                inventory_number=cartridge.inventory_number,
                is_functional=cartridge.is_functional,
                location=location
            )

            # Удаляем из исходной таблицы
            cartridge.delete()

            return redirect('cartridges:cartridge_manage')

    return render(request, 'cartridges/commission.html', {'cartridge': cartridge})

    return render(request, 'commission.html', {'cartridge': cartridge})
class CartridgeUpdateView(UpdateView):
    model = Cartridge
    form_class = CartridgeUpdateForm
    template_name = 'cartridges/cartridge_update.html'
    success_url = '/'

def commissioned_list(request):
    commissioned_cartridges = CommissionedCartridge.objects.all().order_by('-decommissioning_date')
    return render(request, 'cartridges/commissioned_list.html', {
        'commissioned_cartridges': commissioned_cartridges
    })