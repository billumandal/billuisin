from django.contrib import admin
from models import QuizAttempt, QuestionAnswer, UserProfile, Subject

admin.site.register(UserProfile)
admin.site.register(Subject)
admin.site.register(QuestionAnswer)
admin.site.register(QuizAttempt)

class QuestionAnswerAdmin(admin.ModelAdmin):
	list_display = ('subject', 'question_text', 'option_w', 'option_x', 'option_y', 'option_z', 'correct_answer')

class QuizAttemptAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('id', 'subject', 'username', 'total_marks', 'correctly_answered_questions', )}