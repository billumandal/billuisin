from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import QuizAttempt, Question, Answer

class AnswerForm(forms.ModelForm):
	
	# def get_option_w(self, obj):
	# 	return obj.id.option_w
	# def get_option_x(self, obj):
	# 	return obj.id.option_x
	# def get_option_y(self, obj):
	# 	return obj.id.option_y
	# def get_option_z(self, obj):
	# 	return obj.id.option_z
	ANSWER_CHOICES = (
		('option_w', 'Option w'),
		('option_x', 'Option x'),
		('option_y', 'Option y'),
		('option_z', 'Option z'),
	)

	class Meta:
		model = Answer
		correct_answer = forms.MultipleChoiceField(widget=forms.RadioSelect, choices='ANSWER_CHOICES')
		fields = ('id', 'correct_answer',)

# class QuizAttempt(forms.Form):
# 	subject = forms.CharField(max_length=17)
# 	question_text = forms.TextField(max_length=150)
# 	option_w = forms.CharField(max_length=75, null=True)
# 	option_x = forms.CharField(max_length=75, null=True)
# 	option_y = forms.CharField(max_length=75, blank=True)
# 	option_z = forms.CharField(max_length=75, blank=True)
# 	correct_answer = forms.ChoiceField(choices=(('option_w', 'Option w'),
												# ('option_x', 'Option x'),
												# ('option_y', 'Option y'),
												# ('option_z', 'Option z'),), 
# 										widget=forms.RadioSelect(), 
# 										verbose_name='Select your answer')