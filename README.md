Installation

clone files to your project  
```
cd .../project_name
git clone https://github.com/Klyaus/feedback_app
```
Add 'feedback_app' to your config
Make sure that `'django.contrib.staticfiles'` is set up properly and add to `INSTALLED_APPS`
```
INSTALLED_APPS = (
    # ...
    'django.contrib.staticfiles',
    # ...
    'feedback_app',
)

```
'feedback_app' is mostly implemented in a middleware. Enable it in your settings module as follows:
```
MIDDLEWARE_CLASSES  =  ( 
    # ... 
    'feedback_app.middleware.PolMiddleware' , 
    # ... 
)
```
In `urls.py` import views form `feedback_app` and url `feedback_app/`
```
from feedback_app import views
urlpatterns = [
    #...
    path('feedback_app/', views.FeedbackView.as_view()),
]
```

Do not forget to migrate!!!


Configuration
##
FEEDBACK_APP_CONFIG
This dictionary contains all configuration options.

`'insert_before'`

Default: `'</body>'`

'feedback_app' searches for this string in the HTML and inserts itself just before.
##
`'fm_title'`

Default: `'Send message'`

Modal window title text.

##
`'fm_tooltip'`

Default: `'Send an error message or a wish'`

Icon tooltip text

##
`'fm_alert_message'`

Default: `'Message sent!'`

Alert text after sending

##
`'fm_send_button'`

Default: `'Send'`

Button "Send" text

##
`'fm_fields'`

Default: `['name', 'email', 'phone']`

List of fields displayed in the modal window. 
The field "message" - will be displayed necessarily.
##
`'fm_fields_placeholders'`

Must be dictionary

Default: `{"name": "Name", "email": "E-mail", "phone": "Phone", "message": "Enter your message*"}`

Dictionary of fields displayed in the modal window. 
The field "message" - will be displayed necessarily.

Example:
```
FEEDBACK_APP_CONFIG = {
    'insert_before': '</body>',
    'fm_title': 'New message',
    'fm_tooltip': 'Send your message',
    'fm_fields': ['name', 'email'],
    "fm_fields_placeholders": {"name": "Name", "email": "E-mail", "message": "Enter your message*"}
}
```
