import calc

from setuptools import setup, find_packages
from os.path import join, dirname

with open("README.txt", 'r') as f:
    long_description = f.read()

setup(
    name='calc',
    version=calc.__version__,
    author='Egor Bagatyrevich',
    packages=find_packages(),
    install_requires=['flask==2.0.3',
                      'sqlalchemy==1.4.32',
                      'pydantic==1.9.0',
                      'pythondotenv==0.19.2'],
    include_package_data=True,
    description='A module for processing simple calculations.',
    long_description=long_description,
    entry_points={
        'console_scripts':
            ['flask-run = calc.http.flask_server',
             'socket-run = calc.socket.server']
        }
)
