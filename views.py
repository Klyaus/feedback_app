from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from feedback_app.forms import FeedbackForm


class FeedbackView(CreateView):
    form_class = FeedbackForm
    template_name = 'feedback.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user.is_authenticated:
            obj.user = self.request.user
        obj.save()

        return HttpResponse("")
