#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLC',
      version='0.0.1',
      description=('A docassemble extension.'),
      author=u'System Administrator',
      author_email=u'admin@admin.com',
      license='The MIT License (MIT)',
      url='',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['3to2', 'Babel', 'Flask', 'Flask-Babel', 'Flask-KVSession', 'Flask-Login', 'Flask-Mail', 'Flask-SQLAlchemy', 'Flask-SocketIO', 'Flask-User', 'Flask-WTF', 'Jinja2', 'Mako', 'Markdown', 'MarkupSafe', 'Pattern', 'Pillow', 'PyJWT', 'PyPDF2', 'PyYAML', 'Pygments', 'SQLAlchemy', 'SocksiPy-branch', 'WTForms', 'Werkzeug', 'amqp', 'asn1crypto', 'astunparse', 'azure-common', 'azure-nspkg', 'azure-storage', 'bcrypt', 'beautifulsoup4', 'billiard', 'blinker', 'boto', 'celery', 'certifi', 'cffi', 'chardet', 'click', 'cryptography', 'docassemble', 'docassemble.base', 'docassemble.demo', 'docxtpl', 'enum-compat', 'enum34', 'eventlet', 'fdfgen', 'gcs-oauth2-boto-plugin', 'geopy', 'google-api-python-client', 'greenlet', 'guess-language-spirit', 'httplib2', 'idna', 'ipaddress', 'itsdangerous', 'jellyfish', 'kombu', 'links-from-link-header', 'lxml', 'mdx-smartypants', 'namedentities', 'oauth2client', 'olefile', 'passlib', 'pdfminer', 'phonenumbers', 'pkginfo', 'psutil', 'psycopg2', 'pyOpenSSL', 'pyPdf', 'pyasn1', 'pyasn1-modules', 'pycountry', 'pycparser', 'pycrypto', 'pycryptodome', 'pycurl', 'pyotp', 'pyrtf-ng', 'python-dateutil', 'python-docx', 'python-engineio', 'python-socketio', 'pytz', 'qrcode', 'qrtools', 'rauth', 'redis', 'requests', 'requests-toolbelt', 'retry-decorator', 'rsa', 'ruamel.ordereddict', 'ruamel.yaml', 'simplekv', 'six', 'strict-rfc3339', 'tailer', 'textstat', 'titlecase', 'tqdm', 'twilio', 'twine', 'tzlocal', 'ua-parser', 'uritemplate', 'urllib3', 'us', 'user-agents', 'vine'],
      dependency_links=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLC/', package='docassemble.LLC'),
     )

