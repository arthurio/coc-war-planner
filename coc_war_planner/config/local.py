from coc_war_planner.config.settings import *

SECRET_KEY = "Not very secret"

# Send emails to console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ["127.0.0.1"]
