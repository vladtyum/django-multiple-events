from django import forms
from app1.models import EventDate

class EventDateForm(forms.ModelForm):
    class Meta:
        model = EventDate
        fields = ['event', 'pub_date']


# EventDateFormset = inlineformset_factory(
#                         Event, EventDate,
#                         form = EventDateForm,
#                         extra=1
#                         )
