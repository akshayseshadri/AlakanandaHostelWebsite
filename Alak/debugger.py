import local_settings
from local_settings import *

if DEBUG:
    import sys
    import os

    ROOT_FOLDER = os.path.dirname(os.path.realpath(__file__)).split('/')[2] 
    
    if ROOT_FOLDER == "karthikabinav":
        DEBUG_DIR = "/home/karthikabinav/django_workspace/django-debug-toolbar/"
    else:
        DEBUG_DIR = "/home/alakanan/django-debug-toolbar/"

    if not DEBUG_DIR in sys.path:
        sys.path.append(DEBUG_DIR)
    
    TEMPLATE_DIRS = list(TEMPLATE_DIRS)
    TEMPLATE_DIRS.append(DEBUG_DIR + "debug_toolbar/templates")
    TEMPLATE_DIRS = tuple(TEMPLATE_DIRS)

    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES)
    INTERNAL_IPS = ('127.0.0.1')

    DATABASE_ENGINE = 'mysql'
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )


