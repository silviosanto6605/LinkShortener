from setuptools import setup

setup(
    name='LinkShortener',
    version='1.0.0',
    packages=[''],
    url='https://github.com/silviosanto6605/LinkShortener',
    license='MIT',
    author='Silvio Santoriello',
    author_email='silviosanto6605@gmail.com',
    description='LinkShortener will automatically shorten links thanks to tinyurl.com.  You can also make links with custom aliases.',
    install_requires=[
        'requests',
        "multipledispatch",
        'beautifulsoup4'
    ],
)
