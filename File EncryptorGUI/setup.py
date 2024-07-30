# setup.py
from setuptools import setup, find_packages

setup(
    name="file_encryptor_gui",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "cryptography",
        "tk",
    ],
    entry_points={
        'console_scripts': [
            'encryptor_gui=encryptor_gui:main',
        ],
    },
)
