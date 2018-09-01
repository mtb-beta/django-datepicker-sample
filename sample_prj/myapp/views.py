from django.shortcuts import render
from myapp.forms import MyModelForm

def datepicker_view(requests):
    form = MyModelForm()
    return render(requests, 'mymodel_form.html', {'form': form})
