from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    questions = Question.objects.all()
    questions = Question.objects.order_by('?')[:10]
    # Serialise and use the JSON string directly without additional encoding
    questions_json = serializers.serialize('json', questions)
    return render(request, 'cellorganelles/index.html', {'questions_json': questions_json})