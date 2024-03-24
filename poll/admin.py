from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    
    list_display = ('quest_text', 'pub_date', 'was_published_recently')
    
    fieldsets = [
        (None,{'fields': ['quest_text']}),
        ('Date information', {'fields': ['pub_date'], 
                            'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['quest_text']

admin.site.register(Question, QuestionAdmin)


    

