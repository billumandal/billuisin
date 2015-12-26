from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.contrib.auth.models import User 

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
	question_text = models.TextField(max_length=150)
	option_w = models.CharField(max_length=75, blank=True, null=True)
	option_x = models.CharField(max_length=75, blank=True, null=True)
	option_y = models.CharField(max_length=75, blank=True)
	option_z = models.CharField(max_length=75, blank=True)
	on = models.BooleanField(default=True)

	def __unicode__(self):
		return self.id

	class Meta:
		# app_label = 'QuestionAnswer'
		verbose_name='Question'
		verbose_name_plural = 'Questions'

class Answers(models.Model):
	id = models.OneToOneField(QuestionAnswer, primary_key=True)
	correct_answer = models.CharField(max_length=75, blank=False, default=None)

	def __unicode__(self):
		return self.id
		return self.correct_answer

class QuizAttempt(models.Model):
	username = models.ManyToManyField(User)
	subject = models.ManyToManyField(Subject)
	slug = models.SlugField(unique=False)
	datetime = models.DateTimeField(auto_now_add=True)
	questions_included = models.ForeignKey('quiz.QuestionAnswer', null=True)
	correctly_answered_questions = models.IntegerField()
	total_marks = models.IntegerField()

	class Meta:
		verbose_name='Quiz'
		verbose_name_plural = 'Quizzes'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.username +' ' +  self.subject + ' ' + self.datetime.month +' ' +  self.datetime.year)
		super(QuizAttempt, self).save(*args, **kwargs)

	@property
	def correct_answer_count(self):
	    return self._correct_answer_count	

	def __unicode__(self):
		return "Quiz ID is {}".format(self.id)
		return "The quiz was taken by {} on {}".format(self.username, self.topic)
		return "The quiz was taken on {}".format(self.datetime)