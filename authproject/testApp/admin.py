from django.contrib import admin
from testApp.models import quiz
class quizAdminModel(admin.ModelAdmin):
    list_display=['question','choice1','choice2','choice3','choice4','answer']
admin.site.register(quiz,quizAdminModel)

# Register your models here.
