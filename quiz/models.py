from django.db import models
from django.contrib.auth.models import User 
from django.template.defaultfilters import slugify
from django.conf import settings

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	topic = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return self.user.username

class Subject(models.Model):
	subject_name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.subject_name

class QuestionAnswer(models.Model):
	subject = models.ManyToManyField(Subject)
	question_text = models.CharField(max_length=150)
	option_w = models.CharField(max_length=75, null=True)
	option_x = models.CharField(max_length=75, null=True)
	option_y = models.CharField(max_length=75, blank=True)
	option_z = models.CharField(max_length=75, blank=True)
	correct_answer = models.CharField(max_length=75, blank=False)

	def __unicode__(self):
		return self.id

	class Meta:
		verbose_name='Question'
		verbose_name_plural = 'Questions'

# class Answer(models.Model):
# 	question = models.OneToOneField(Question)
# 	correct_answer = models.CharField(max_length=75, blank=False)

class QuizAttempt(models.Model):
	username = models.ManyToManyField(User)
	subject = models.ManyToManyField(Subject)
	slug = models.SlugField(unique=False)
	datetime = models.DateTimeField(auto_now_add=True)
	questions_included = models.ManyToManyField(QuestionAnswer)
	correctly_answered_questions = models.IntegerField()
	total_marks = models.IntegerField()

	class Meta:
		verbose_name='Quiz'
		verbose_name_plural = 'Quizzes'

	@property
	def correct_answer_count(self):
	    return self._correct_answer_count
	

	def __unicode__(self):
		return "Quiz ID is {}".format(self.id)
		return "The quiz was taken by {} on {}".format(self.username, self.topic)
		return "The quiz was taken on {}".format(self.datetime)
