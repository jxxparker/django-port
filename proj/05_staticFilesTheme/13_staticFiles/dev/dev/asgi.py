from ast import AsyncFunctionDef
from calendar import firstweekday
from lib2to3.pgen2.pgen import DFAState
import os
from signal import SIG_DFL

from django.core.asgi import get_asgi_application
from django.test import skipUnlessAnyDBFeature
from numpy import DataSource
from platformdirs import site_data_dir

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev.settings')

application = get_asgi_application()
