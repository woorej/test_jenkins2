from setuptools import setup, find_packages
import os

this_directory = os.path.abspath(os.path.dirname(__file__))

version_path = os.path.join(this_directory, 'calcul', '__init__.py')

with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
with open(os.path.join(this_directory, 'requirements.txt')) as f:
    required = f.read().splitlines()


with open(version_path) as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith('__version__'):
            version_line = line
            break

exec(version_line)

setup(
    name="calcualtor",
    version = __version__,
    author='woojae',
    description='test_jenkins_model',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='jwj@hims.co.kr',
    url='https://github.com/woorej/test_jenkins2.git',
    install_requires=required,
    package_dir={'':'.'},
    packages=find_packages(where='.'), 
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'calcul-ai=calcul.calculator_server:main',
        ],
    },
    zip_safe=False,
    package_data={},
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
    ]
)