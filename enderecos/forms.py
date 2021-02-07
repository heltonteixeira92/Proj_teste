from django import forms
from localflavor.br.forms import BRZipCodeField


class AddressForm(forms.Form):
    zip_code = BRZipCodeField(label='CEP', max_length=9)
    street = forms.CharField(label='Rua', max_length=100)
    district = forms.CharField(label='Bairro', max_length=100)
    city = forms.CharField(label='Cidade', max_length=100)
    state = forms.CharField(label='Estado', max_length=100)
