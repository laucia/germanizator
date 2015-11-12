from distutils.core import setup

setup(
    name='germanizator',
    version='0.0.1',
    description='A terrible library to transform english into phonetic german',
    author = "Johnny Lee Othon, Lauris Jullien",
    author_email='jleeothon@gmail.com, lauris.jullien@gmail.com',
    packages=['germanizator'],
    requires=[
        'requests (>=2.8.0)',
        'lxml (>=3.4.0)',
    ]
)
