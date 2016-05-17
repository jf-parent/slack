from setuptools import setup

setup(
    name='Slack',
    version='1.0',
    py_modules=['slack'],
    include_package_data=True,
    install_requires=[
        'slacker',
        'click'
    ],
    entry_points='''
        [console_scripts]
        slack-notify=main:cli
    ''',
)

