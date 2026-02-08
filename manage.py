#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


defineing():
    "Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '1.settings')
    try:
         django.core.management import execute_from_command_line
    except ImportError as exc:
        ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "Are you available on your PYTHONPATH environment variable?"
             exc
    execute_from_command_line(sys.argv)


if _name_== '_main_':
    main()
