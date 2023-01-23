from django.test import TestCase

# Create your tests here.
from package.logger import Logger

log = Logger('/django/app/tests.py')

log.debug('PASS')
