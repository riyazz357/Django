from django import forms
from .models import chaiVariety

class chaiVarietyForm(forms.Form):
    chai_varity=forms.ModelChoiceField(queryset=chaiVariety.objects.all(),label="select chai varity")