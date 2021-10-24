from django.shortcuts import render, redirect
from .models import List
from .models import Contact
from .models import profile
from .forms import ListForm, EditForm, ContactForm, profileForm
from django.contrib import messages



def home(request):
         if request.method == 'POST':
                  form = ListForm(request.POST or None)
                  if form.is_valid():
                           form.save()
                           all_items = List.objects.all()
                           context = {'all_items': all_items, "user" : "Rhee"}
                           return render(request, 'home.html', context)
                  else:
                           all_items = List.objects.all()
                           context = {'all_items' : all_items ,"user" : "Rhee"}
                           return render(request, 'home.html', context)  
         else:
                  all_items = List.objects.all()
                  context = {'all_items' : all_items,"user" : "Rhee"}
                  return render(request, 'home.html', context)
         
def about(request):
         my_name = "Rhee Pogi"
         return render(request, 'about.html',{"myname" : my_name})

def contact(request):
         if request.method == 'POST':
                  form = ContactForm(request.POST or None)
                  if form.is_valid():
                           form.save()
                           all_cont = Contact.objects.all()
                           context = {"all_cont" : all_cont}
                           return render(request, 'contact-us.html', context)
                  else:
                            all_cont = Contact.objects.all()
                            context = {"all_cont" : all_cont}
                            return render(request, 'contact-us.html', context)
         else:
                  all_cont = Contact.objects.all()
                  context = {"all_cont" : all_cont}
                  return render(request, 'contact-us.html', context)
         

def delete(request, list_id):
         item = List.objects.get(pk=list_id)
        # pracname = prac.objects.get(pk=list_id)
      #  pracname.delete()
         item.delete()
         return redirect('home')

def deletecont(request, cont_id):
         cont = Contact.objects.get(pk=cont_id)
         cont.delete()
         return redirect('contact')

def strike(request, list_id):
         item = List.objects.get(pk=list_id)
         item.completed = True
         item.save()
         return redirect('home')

def unstrike(request, list_id):
         item = List.objects.get(pk=list_id)
         item.completed = False
         item.save()
         return redirect('home')

def listings(request):
         if request.method == 'POST':
                  form = ListForm(request.POST or None)
                  if form.is_valid():
                           form.save()
                           all_items = List.objects.all()
                           all_prac = prac.objects.all()
                           context = {'all_items': all_items, 'all_prac':all_prac, "user" : "Rhee"}
                           return render(request, 'home.html', context)
                  else:
                           all_items = List.objects.all()
                           all_prac = prac.objects.all()
                           context = {'all_items' : all_items, 'all_prac' : all_prac, "user" : "Rhee"}
                           return render(request, 'home.html', context)  
         else:
                  all_items = List.objects.all()
                  all_prac = prac.objects.all()
                  context = {'all_items' : all_items, 'all_prac' : all_prac, "user" : "Rhee"}
                  return render(request, 'home.html', context)  

def edit(request, list_id):
         if request.method=='POST':
                  list_item = List.objects.get(pk=list_id)
                  form = EditForm(request.POST or None)
                  if form.is_valid():
                           updated_item=form.cleaned_data.get("item")
                           list_item.item= updated_item
                           list_item.save()
                           return redirect('home')
         else:
                  list_item = List.objects.get(pk=list_id)
                  context= {"list_id": list_id, "list_item": list_item}
                  return render(request, 'edit.html', context)

#-------------------------------------------------------------------------------------------------------------

def addprofile(request):
  if request.method == 'POST':
    form = profileForm(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect('addcontact')
    else:
      messages.error(request, 'PLEASE FOLLOW REQUIRED INPUTS')
      return render(request, 'addprofile.html', {})

  return render(request, 'addprofile.html', {})
  

'''
def addprofile(request):
  if request.method == 'POST':
    form = profileForm(request.POST or None)
    if form.is_valid():
      form.save()
      queryset = profile.objects.last()
      profile_id = queryset.id
      #context = {'profile_id' : profile_id}
      return redirect('addcontact')
    else:
      form = profileForm(request.POST or None)
      context = {'form': form}
      return render(request, 'addprofile.html', context)


  return render(request, 'addprofile.html', {})

'''

def addcontact(request):
  '''
  p_id = 0
  try:
    prof_id = profile.objects.last()
    p_id = prof_id.id
  except Exception as nt:
    p_id = 1
  finally:
    p_id = int(p_id)  
  context = {'p_id': p_id }
  '''
  prof_id = profile.objects.last()
  p_id = prof_id.id
  p_id = int(p_id)
  context = { 'p_id': p_id } 
  if request.method == 'POST':
    form = ContactForm(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect('home')

  return render(request, 'addcontact.html', context)




# Create your views here.
