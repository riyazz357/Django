from django.shortcuts import render
from .models import chaiVariety,Store
from django.shortcuts import get_object_or_404
from .forms import chaiVarietyForm

# Create your views here.
def all_chai(request):
    chais= chaiVariety.objects.all #this will query on the given model and put it in chai and it will give array

    return render(request,'chai/all_chai.html',{"chais":chais})

def chai_detail(request, chai_id):
    chai=get_object_or_404(chaiVariety,pk=chai_id)
    return render(request,'chai/chai_detail.html',{'chai':chai})

def chai_store_views(request):
    stores=None
    if request.method=='POST':
        form=chaiVarietyForm(request.POST)
    if form.is_valid():
        chai_variety=form.cleaned_data['chai_varity']

    return render(request,'chai/chai_stores.html',{stores})