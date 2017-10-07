from django.shortcuts import render, redirect
from django import forms
from app1.forms import EventDateForm
from app1.models import EventDate



def home(request):
    eventsdate_list = EventDate.objects.order_by('-pub_date')
    context = {'eventsdate_list': eventsdate_list}
    return render(request, 'app1/index.html', context)


def add_event(request):
    if request.method == "POST":
        form = EventDateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EventDateForm()
        return render(request, 'app1/add-event.html',
                        {
                        'form':form,
                        }
                    )
