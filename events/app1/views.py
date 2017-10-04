from django.shortcuts import render
# from .models import Question


def home(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    context = {}
    return render(request, 'app1/index.html', context)
