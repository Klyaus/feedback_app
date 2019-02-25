from functools import lru_cache

from django.conf import settings

CONFIG_DEFAULTS = {
    'insert_before': '</body>',
    'fm_title': 'New message',
    'fm_tooltip': 'Send an error message or a wish',
    'fm_alert_message': 'Message sent!',
    'fm_send_button': 'Send',
    'fm_fields': ['name', 'email', 'phone'],
    'fm_fields_placeholders': {'name': 'Name', 'email': 'E-mail', 'phone': 'Phone', 'message': 'Enter your message*'},
}


@lru_cache()
def get_config():
    user_config = getattr(settings, 'FEEDBACK_APP_CONFIG', {})

    config = CONFIG_DEFAULTS.copy()
    config.update(user_config)
    return config
