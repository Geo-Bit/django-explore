from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline): # represent the choices in the question creation page.
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text'] # controls the order of the fields on the Question admin page.
    fieldsets = [ # Use field sections
        (None,               {'fields':['question_text']}),
        ('Date Information', {'fields':['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date'] # adds a filter sidebar to the Question Admin page for pub_date
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
