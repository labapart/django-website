#!/usr/bin/python
# encoding: utf-8

import os, sys

"""
deploy.cgi: Script to deploy Django website on the web hosting solution

Copyright (c) 2015 - Lab A Part
Olivier <olivier@labapart.com>

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

WWW_PATH = os.path.dirname(os.path.abspath(__file__))
DJANGO_PROJECT_PATH = os.path.dirname(WWW_PATH)

sys.path.append(DJANGO_PROJECT_PATH + "/django-1.6.11")
sys.path.append(DJANGO_PROJECT_PATH + "/django-1.6.11/django/bin/")
sys.path.append(DJANGO_PROJECT_PATH + "/django-1.6.11/django/")
sys.path.append(DJANGO_PROJECT_PATH + "/")
sys.path.append(DJANGO_PROJECT_PATH + "/httplib2-0.9.2/python2")
sys.path.append(DJANGO_PROJECT_PATH + "/mysite/") #TODO: Update me if the name of the Django application is different
sys.path.append(DJANGO_PROJECT_PATH + "/mysite/mysite/") #TODO: Update me if the name of the Django application is different
sys.path.append(DJANGO_PROJECT_PATH + "/six-1.10.0")
sys.path.append(DJANGO_PROJECT_PATH + "/South-1.0.2")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.production")  #TODO: Update me if the name of the production settings are different
from django.core.management import call_command

print("Content-type: text/html\n\n")

try:
	call_command('syncdb', interactive=False)
	call_command('collectstatic', interactive=False)
except Exception, inst:
    print(inst)
