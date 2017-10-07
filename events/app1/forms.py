from django import forms
from app1.models import EventDate
from django.forms import formset_factory

class EventDateForm(forms.ModelForm):
    class Meta:
        model = EventDate
        fields = ['event', 'pub_date']


EventDateFormset = formset_factory(EventDateForm, extra=2)
