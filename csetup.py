from distutils.core import setup
from Cython.Build import cythonize
import sys, os
from setuptools import setup
import subprocess
from distutils.command.install import install as DistutilsInstall

"""
python csetup.py build_ext --inplace
"""

__version__ = "0.9.5"

def readme():
    with open('README.md') as f:
        return f.read()

class MyInstall(DistutilsInstall):
    def run(self):
        # do_pre_install_stuff()
        DistutilsInstall.run(self)
        # do_post_install_stuff()
        self.CMakeInstall(command="make")

    def CMakeInstall(self, command):
        make_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=sys.stdout.fileno())
        while True:
            line = make_process.stdout.readline()
            if not line:break
            print(line) #output to console in time
            sys.stdout.flush()

setup(
    name = "pics2word",
    description='A command line program to copy pictures into a word document.',
    version=__version__,
    url='https://github.com/Ghostom998/pics2word.git',
    author='Thomas Roberts',
    author_email='tom_roberts.1992@hotmail.co.uk',
    license='GNU GPL V3.0',
    packages=['pics2word'],
    install_requires=['docx','python-docx','datetime'],
    python_requires='>=3.6.4',
    include_package_data=True,
    zip_safe=True,
    long_description=readme(),
    ext_modules = cythonize("cython-port/*.pyx"),
    cmdclass={'install': MyInstall},
    entry_points = {
        'console_scripts': ['pics2word=pics2word.__init__:main'],
    },
    classifiers=[
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3.6',
    'Environment :: Console',
    'Topic :: Office/Business :: Office Suites',
    ]
)