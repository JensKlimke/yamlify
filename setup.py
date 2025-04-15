from setuptools import setup, find_packages

setup(
    name='datify',
    version='0.1.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'markdown',
        'pyyaml',
        'Jinja2'
    ],
    entry_points={
        'console_scripts': [
            'datify=datify:main',
        ],
    },
)
