from setupstools import setup

setup(
    name = 'jussi'
    version = '0.1.0'
    packages = ['jussi']
    entry_points = {
                    'console_scripts': [
                        'jussi = jussi.__main__:main'
                    ]
                })
                
