try:
    from project.local_settings import *
except ImportError:
    from project.default_settings import *
