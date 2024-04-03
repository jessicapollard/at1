from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required

# Decorate the view function to ensure it's accessible only to logged-in users
@login_required
def index(request):
    questions = Question.objects.all() # Retrieve all questions from the database
    questions = Question.objects.order_by('?')[:10] # Order questions randomly and limit to 10
    # Serialise and use the JSON string directly without additional encoding
    questions_json = serializers.serialize('json', questions)
    return render(request, 'cellorganelles/index.html', {'questions_json': questions_json})