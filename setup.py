from setuptools import setup

setup(
    name='LinkShortner',
    version='1.0.1',
    packages=[''],
    url='https://github.com/silviosanto6605/LinkShortner',
    license='MIT',
    author='Silvio Santoriello',
    author_email='silviosanto6605@gmail.com',
    description='LinkShortner will automatically shorten links thanks to tinyurl.com.  You can also make links with custom aliases.',
    install_requires=[
        'requests',
        "multipledispatch",
        'beautifulsoup4'
    ],
)
