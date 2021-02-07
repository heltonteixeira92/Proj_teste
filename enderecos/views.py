# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import AddressForm


class AddressFormView(FormView):
    form_class = AddressForm
    success_url = reverse_lazy('enderecos:enderecos')
    template_name = 'enderecos/enderecos.html'
