# chatbot/views.py
from django.shortcuts import render
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from .models import Question, Response

def get_response_from_database(user_input):
    questions = Question.objects.all()
    matched_question, score = process.extractOne(user_input, [q.text for q in questions])

    # You can adjust the threshold as needed
    if score >= 50:
        # If the similarity score is above a certain threshold, retrieve the response
        try:
            question = Question.objects.get(text__iexact=matched_question)
            response = Response.objects.get(question=question)
            return response.text
        except Question.DoesNotExist:
            return "I'm sorry, I don't know the answer to that question."
        except Response.DoesNotExist:
            return "I don't have a response for that question yet."
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = get_response_from_database(user_input)
        return render(request, 'chatbot/chatbot.html', {'user_input': user_input, 'response': response})

    return render(request, 'chatbot/chatbot.html')