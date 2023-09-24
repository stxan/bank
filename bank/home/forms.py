from django import forms


class TransferForm(forms.Form):
    receiver_username = forms.CharField(max_length=100)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
