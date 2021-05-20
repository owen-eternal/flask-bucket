from typing import Text
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='Flask-bucket',
    version='0.0.1',
    url='https://github.com/owen-eternal/flask-bucket',
    license='BSD',
    author='Owen O. Phakade',
    author_email='olwethuphakade89@gmail.com',
    description='Create flask modules using a flask shell command',
    long_description=long_description,
    long_description_content_type="Text/markdown",
    py_modules=['Flask_bucket'],
    package_dir={'': 'flask-bucket'},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    extras_require={"dev" : [
        "pytest>=3.7"     
    ]},

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python >= 3.6+',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)