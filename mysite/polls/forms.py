from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)




from django import forms

from datetime import date

class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

from django.forms import formset_factory
from django.shortcuts import render





def form_view(request):
    ArticleFormSet = formset_factory(ArticleForm)

    formset = ArticleFormSet(
    #initial=[{'title': 'Django is now open source','pub_date': date.today(),}]
    )
    to_pass = ""
    
    
    for form in formset:
        to_pass+=form.as_table()
    
    
    return render(request, "to_pass.html", {"forms": []})
