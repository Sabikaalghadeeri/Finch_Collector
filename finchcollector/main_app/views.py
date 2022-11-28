from django.shortcuts import render, redirect
from django.http import HttpResponse
# main_app/views.py
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm


def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)


class FinchUpdate(UpdateView):
  model = Finch
  fields = '__all__'
  success_url = '/finchs/'
  
  
class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finchs/'

  
  
class FinchCreate(CreateView):
  model = Finch
  fields = '__all__' 
  success_url = '/finchs/'
  
  
  

def finchs_detail(request, finch_id):
  finch = Finch.objects.get(id = finch_id)
  
  feeding_form = FeedingForm()
  
  return render (request, 'detail.html', {'finch': finch, 'feeding_form': feeding_form})



def finchs_index(request):
    finchs_list = Finch.objects.all()
    return render(request, 'finchs/index.html', {'Finchs': finchs_list})

def about(request):
  return render(request, 'about.html')
# Define the home view
def home(request):
    return render(request, 'home.html')
  
  # return HttpResponse('<h1>Hello Finch Bird</h1>')

# def about(request):
#     return HttpResponse('<h1>About My Finchs</h1>') 