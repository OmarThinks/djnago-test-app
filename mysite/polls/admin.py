from django.contrib import admin
# Register your models here.

from .models import Question, Choice, Blog, Author, Entry, Customer



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ] # Divide them into groups
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date', "question_text"]
    search_fields = ['question_text']



class ChoiceAdmin(admin.ModelAdmin):
    fields= ["question_text", "pub_date"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Customer)


