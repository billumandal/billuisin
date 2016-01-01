from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	GENDER_CHOICE = (
		('M', 'Male'),
		('Fem', 'Female'),
		('Others', 'Others')
	)
	SUBJECTS = (
		('java', 'Java'),
		('dotnet','Asp.net'),
		('php','PHP'),
		('testing','Software Testing'),
		('python', 'Python'),
		('ruby','Ruby on Rails'),
		('cbasic', 'C Basic'),
		('oops', 'Object Oriented Programming'),
	)

	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	birth_date = models.DateField()
	phone_number = models.CharField(max_length=10)
	gender = models.CharField(max_length=30, choices=GENDER_CHOICE, null=True)
	address = models.CharField(max_length=150, null=True)
	postal_code = models.PositiveIntegerField(null=True)
	# Have to pull subjects from the subject class here, and more than one 
	subject_name = models.CharField(choices=SUBJECTS, null=True, verbose_name='Name of subject(s)', max_length=17)

	def __unicode__(self):
		return self.user

	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance)

	post_save.connect(create_user_profile, sender=User)

	# def user_subject_name(self):
	# 	return self.user.subject_name

class Subject(models.Model):
	SUBJECTS = (
		('java', 'Java'),
		('dotnet','Asp.net'),
		('php','PHP'),
		('testing','Software Testing'),
		('python', 'Python'),
		('ruby','Ruby on Rails'),
		('cbasic', 'C Basic'),
		('oops', 'Object Oriented Programming'),
	)

	subject_name = models.CharField(choices=SUBJECTS, null=True, verbose_name='Name of subject(s)', max_length=17)

	def __unicode__(self):
		return self.subject_name

class Question(models.Model):
	subject = models.ManyToManyField(Subject)
	question_text = models.TextField(max_length=150)
	option_w = models.CharField(max_length=75, blank=True, null=True)
	option_x = models.CharField(max_length=75, blank=True, null=True)
	option_y = models.CharField(max_length=75, blank=True)
	option_z = models.CharField(max_length=75, blank=True)
	on = models.BooleanField(default=True)

	def __unicode__(self):
		return "{} -> {}".format(self.id, self.question_text)

	class Meta:
		# app_label = 'Question'
		verbose_name='Question'
		verbose_name_plural = 'Questions'


class Answer(models.Model):
	
	id = models.OneToOneField(Question, primary_key=True)

	ANSWER_CHOICES = (
		('get.option_w', 'get.option_w'),
		('get.option_x', 'get.option_x'),
		('get.option_y', 'get.option_y'),
		('get.option_z', 'get.option_z'),
	)
	def get_option_w(self, obj):
		return obj.id.option_w
	def get_option_x(self, obj):
		return obj.id.option_x
	def get_option_y(self, obj):
		return obj.id.option_y
	def get_option_z(self, obj):
		return obj.id.option_z

	correct_answer = models.CharField(max_length=75, blank=False, default=None, choices=ANSWER_CHOICES)

	def __unicode__(self):
		return "The correct answer for question {} is {}".format( self.id, self.correct_answer)

class QuizAttempt(models.Model):
	username = models.ManyToManyField(User)
	subject = models.ManyToManyField(Subject)
	slug = models.SlugField(unique=False)
	datetime = models.DateTimeField(auto_now_add=True)
	questions_included = models.ForeignKey('quiz.Question', null=True)
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