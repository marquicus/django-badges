__doc__ = """
An easy to use app that provides Stack Overflow style badges with a minimum ammount of effort in django

See the README file for details, usage info, and a list of gotchas.
"""

from setuptools import setup

setup(
    name='django-badges',
    version='1.1.2',
    author='James Robert',
    author_email='jiaaro@gmail.com',
    description=('An easy to use app that provides Stack Overflow style badges \
        with a minimum ammount of effort in django'),
    license='GPLv3',
    keywords='django badges social',
    url='http://djangobadges.com',
    packages=['badges', 'badges.templatetags', 'badges.migrations', 'badges.templates'],
    package_data={'badges': ['badges/templates/badges/*.html']},
    install_requires=[
        "django >= 2.0",
        "Pillow",
        "future",
        "tox-pyenv",
    ],
    long_description=__doc__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ]
)
