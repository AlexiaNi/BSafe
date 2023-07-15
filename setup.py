from setuptools import setup

setup(
   name='BSafe',
   version='1',
   description='BSafe Password Manager',
   author='Niculae Alexia',
   packages=['BSafe'],  #same as name
   install_requires=['tkinter', 'sqlite3', 'PIL', 'os', 'hashlib', 'configparser'], 
)
