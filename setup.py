from setupstools import setup

setup(
    name = 'learning-click'
    version = '0.1.0'
    packages = ['learning-click']
    entry_points = {
                    'console_scripts': [
                        'learning-click = learning-click.__main__:main'
                    ]
                })
                
