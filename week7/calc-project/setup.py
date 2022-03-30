import calc1

from setuptools import setup, find_packages
from os.path import join, dirname

with open("README.txt", 'r') as f:
    long_description = f.read()

setup(
    name='calc',
    version=calc.__version__,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    entry_points={
        'console_scripts':
            ['flask-run = calc.http.flask_server',
             'socket-run = calc.socket.server']
        }
)
