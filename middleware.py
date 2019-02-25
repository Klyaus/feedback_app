import re

from django.middleware.csrf import get_token
from django.template.loader import render_to_string
from django.utils.deprecation import MiddlewareMixin
from django.utils.encoding import force_text
from feedback_app.forms import FeedbackForm
from feedback_app import settings as feedback_app_settings


class FeedbackMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        form = FeedbackForm(request.POST)
        content = force_text(response.content, encoding=response.charset)
        insert_before = feedback_app_settings.get_config()["insert_before"]
        pattern = re.escape(insert_before)
        bits = re.split(pattern, content, flags=re.IGNORECASE)
        csrf_token_value = get_token(request)
        fm_title = feedback_app_settings.get_config()["fm_title"]
        fm_tooltip = feedback_app_settings.get_config()["fm_tooltip"]
        fm_alert_message = feedback_app_settings.get_config()["fm_alert_message"]
        fm_send_button = feedback_app_settings.get_config()["fm_send_button"]
        context = {'form': form, 'csrf_token': csrf_token_value, 'fm_title': fm_title,
                   'fm_tooltip': fm_tooltip, 'fm_alert_message': fm_alert_message, 'fm_send_button': fm_send_button}
        page = render_to_string("feedback.html", context)
        if len(bits) > 1:
            bits[-2] += page
            response.content = insert_before.join(bits)
        return response
