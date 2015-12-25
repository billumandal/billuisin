from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import QuizAttempt

class QuizAttempt(forms.Form):
	subject = forms.ManyToManyField(Subject)
	question_text = forms.CharField(max_length=150)
	option_w = forms.CharField(max_length=75, null=True)
	option_x = forms.CharField(max_length=75, null=True)
	option_y = forms.CharField(max_length=75, blank=True)
	option_z = forms.CharField(max_length=75, blank=True)
	correct_answer = forms.ChoiceField(choices=(('a)', option_w),
												('b)', option_x),
												('c)', option_y),
												('d)', option_z),), 
										widget=forms.RadioSelect(), 
										verbose_name='Select your answer')