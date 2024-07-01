from django import forms


class classForm (forms.Form):
    money = forms.CharField(max_length=100, required=True)
    product = forms.IntegerField(required=True)




    