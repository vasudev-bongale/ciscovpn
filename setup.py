from setuptools import setup

setup(
    name='ciscovpn',
    version='0.1.0',
    packages=['ciscovpn'],
    author='Vasudev Bongale',
    author_email='vasudev2111@gmail.com',
    license='MIT',
    install_requires=[
        'pexpect',
        'keyring',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'ciscovpn = ciscovpn.ciscovpn:main'
        ]
    })
