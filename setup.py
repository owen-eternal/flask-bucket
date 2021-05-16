from setuptools import setup

setup(
    name='Flask-bucket',
    version='0.0.1',
    url='https://github.com/owen-eternal/flask-bucket',
    license='BSD',
    author='Owen O. Phakade',
    author_email='olwethuphakade89@gmail.com',
    description='Create flask modules using a flask shell command',
    long_description=__doc__,
    py_modules=['Flask_bucket'],
    package_dir={'': 'flask-bucket'},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
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