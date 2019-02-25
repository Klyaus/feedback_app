from django import forms
from feedback_app.models import Feedback
from feedback_app import settings as feedback_app_settings


class FeedbackForm(forms.ModelForm):
    class Meta(object):
        model = Feedback
        fields = feedback_app_settings.get_config()["fm_fields"]
        fields_placeholders = feedback_app_settings.get_config()["fm_fields_placeholders"]
        fields.append('message')
        widgets = {}
        for field in fields:
            if field == 'name':
                widgets['name'] = forms.TextInput(
                    attrs={
                        'class': 'uk-input',
                        'placeholder': fields_placeholders[field],
                        'type': 'text'
                    })
            if field == 'email':
                widgets['email'] = forms.EmailInput(
                    attrs={
                        'class': 'uk-input',
                        'placeholder': fields_placeholders[field],
                        'type': 'email'
                    })
            if field == 'phone':
                widgets['phone'] = forms.TextInput(
                    attrs={
                        'class': 'uk-input',
                        'placeholder': fields_placeholders[field],
                        'type': 'text'
                    })
            if field == 'message':
                widgets['message'] = forms.Textarea(
                    attrs={
                        'class': 'uk-textarea',
                        'placeholder': fields_placeholders[field],
                        'rows': '5',
                        'required': True
                    })
