from django.shortcuts import render
import simplejson as json

# Create your views here.
def get_client_ip(request):
# Here try to move the page forward only if it matches Technnovation's ip.
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split('.')[-1].strip()
	else:
		ip = request.META.get('REMOTE_ADDR')

	if ip = '61.17.77.127':
			# Let the user go on to do the quiz
	else:
			# Tell him to do this test inside Technnovation Labs


def QuizAttempt(request):
	if request.method == 'POST':
		form = QuizAttempt(request.POST)
		if form.is_valid():
			correct_answer = form.cleaned_data.get('correct_answer')
			# Do something with teh results 
			
			return HttpResponseRedirect('/next_question_here/')

		return render_to_response('question.html', {'form': form})

		
