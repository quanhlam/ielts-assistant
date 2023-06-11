#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging

from django.core.cache import cache

from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bag_api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Verify Redis connection
    try:
        redis_client = cache.client.get_client(write=True)
        if redis_client.ping():
            logging.info('Successfully connected to Redis')
        else:
            logging.warning('Failed to connect to Redis')
    except:
        logging.warning('Failed to connect to Redis')

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
