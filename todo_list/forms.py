from django import forms
from .models import List
from .models import Contact
from .models import profile
from django.core.exceptions import ValidationError

profile_type_choices = {'Patient', 'Employee'}

class ListForm(forms.ModelForm):
         class Meta:
                  model = List
                  fields = ['item', 'completed']

class EditForm(forms.ModelForm):
         class Meta:
                  model = List
                  fields = ['item'] 

class ContactForm(forms.ModelForm):
         class Meta:
                  model = Contact
                  fields= ['prof_id', 'c_name' ,'c_address']

class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['fullname', 'address', 'profile_type', 'bday', 'age', 'deci_number']
    '''
    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        if not "Rhee" in fullname:
            raise forms.ValidationError("Rhee is the only answer")
        else:
            return fullname
    '''