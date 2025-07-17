from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from .forms import CartridgeCreateForm,CartridgeUpdateForm
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
            return redirect('/')
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


def commission(request, pk):
    cartridge = get_object_or_404(Cartridge, pk=pk)

    if request.method == 'POST':
        location = request.POST.get('location', '').strip()
        cartridge.expl_by = request.user

        if location:
            CommissionedCartridge.objects.create(
                name=cartridge.name,
                device_name=cartridge.device_name,
                acceptance_date=cartridge.acceptance_date,
                decommissioning_date=cartridge.decommissioning_date or date.today(),
                inventory_number=cartridge.inventory_number,
                is_functional=cartridge.is_functional,
                location=location,
                expl_by= request.user
            )

            cartridge.delete()

            return redirect('cartridges:commissioned_list')

    return render(request, 'cartridges/commission.html', {'cartridge': cartridge})


def commissioned_list(request):
    commissioned_cartridges = CommissionedCartridge.objects.all().order_by('-decommissioning_date')
    return render(request, 'cartridges/commissioned_list.html', {
        'commissioned_cartridges': commissioned_cartridges
    })


class Search(ListView):
    model = Cartridge
    template_name = 'cartridges/main.html'
    context_object_name = 'cartridges'

    def get_queryset(self):
        name_query = self.request.GET.get('name', '')
        device_query = self.request.GET.get('device', '')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        inv_number_query = self.request.GET.get('inventory_number','')
        user_query = self.request.GET.get('added_by', '')
        user_id = self.request.GET.get('user')

        queryset = Cartridge.objects.all()

        if name_query:
            queryset = queryset.filter(name__icontains=name_query)
        if device_query:
            queryset = queryset.filter(device_name__icontains=device_query)
        if date_from:
            queryset = queryset.filter(acceptance_date__gte=date_from)
        if date_to:
            queryset = queryset.filter(acceptance_date__lte=date_to)
        if inv_number_query:
            queryset = queryset.filter(inventory_number__icontains=inv_number_query)
        if user_query:
            queryset = queryset.filter(added_by__icontains=inv_number_query)
        if user_id:
            queryset = queryset.filter(added_by_id=user_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        User = get_user_model()
        context['name_query'] = self.request.GET.get('name', '')
        context['device_query'] = self.request.GET.get('device', '')
        context['users'] = User.objects.all()
        context['selected_user'] = self.request.GET.get('user', '')
        return context