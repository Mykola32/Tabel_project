from django import forms

class FormBuyer(forms.Form):
    t_del = (('1', 'вантажівка'),
             ('2', 'дрон'),
             ('3', 'авіа'))
    distance = forms.FloatField(label='Відстань, км:')
    type_delivery = forms.ChoiceField(choices=t_del, label='Вибір:')
    masa = forms.FloatField(label='Маса вантажу, кг:')
    pib = forms.CharField(label='ПІБ отримувача:')
    phone = forms.CharField(label='phone:', initial='+380', min_length=13, max_length=13)
    email = forms.EmailField(label='email:')
