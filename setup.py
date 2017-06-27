try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Minesweeper for coding practice',
    'author': 'Howard Kim',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'howardwkim@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['minesweeper'],
    'scripts': [],
    'name': 'minesweeper'
}

setup(**config)
