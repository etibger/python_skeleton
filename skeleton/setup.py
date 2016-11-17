""" Setup file for NAME moduel """
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

SETUP_CONFIG = {
    'description': 'My Project',
    'author': 'Tibor Gerlai',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'tibi.gerlai@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**SETUP_CONFIG)
