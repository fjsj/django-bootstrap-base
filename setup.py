from setuptools import setup, find_packages

setup(
    name='django-bootstrap-base',
    version=__import__('bootstrap_base').__version__,
    description='This provides a base template bootstrap_base/html5pb.html for your own base_site.html to extend.',
    long_description=open('README.md').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='crucialfelix',
    author_email='crucialfelix@github.com',
    url='https://github.com/crucialfelix/django-bootstrap-base',
    download_url='https://github.com/crucialfelix/django-bootstrap-base/downloads',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
