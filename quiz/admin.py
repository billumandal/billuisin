from django.contrib import admin
from django.contrib.auth.models import User
from models import QuizAttempt, Question, Answer, UserProfile
from forms import AnswerForm

class UserProfileAdmin(admin.ModelAdmin):
	def user_subject_name(self, instance):
		return instance.user.subject_name
	
	list_display = ('user', 'subject_name', 'phone_number')
	search_fields = ('user',)
	list_filter = ('subject_name', )

# class AnswerAdmin(admin.ModelAdmin):
	# def get_option_w(self, obj):
	# 	return obj.id.option_w
	# def get_option_x(self, obj):
	# 	return obj.id.option_x
	# def get_option_y(self, obj):
	# 	return obj.id.option_y
	# def get_option_z(self, obj):
	# 	return obj.id.option_z
		
	# ANSWER_CHOICES = (
	# 	('option_w', 'Option w'),
	# 	('option_x', 'Option x'),
	# 	('option_y', 'Option y'),
	# 	('option_z', 'Option z'),
	# )

# 	model = Answer
# 	list_display = ('correct_answer')

class AnswerInline(admin.TabularInline):
	model = Answer

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text','id',)
	fields = ('subject', 'question_text', 'option_w', 'option_x', 'option_y', 'option_z')
	inlines = [
		AnswerInline,
	]

class QuizAttemptAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('id', 'subject', 'username', 'total_marks', 'correctly_answered_questions', )}
	list_filter = ('datetime', 'subject_name', 'total_marks',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizAttempt)