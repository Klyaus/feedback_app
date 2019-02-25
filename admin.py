from django.contrib import admin
from feedback_app.models import *


# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'create_date', 'name', 'message']

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
