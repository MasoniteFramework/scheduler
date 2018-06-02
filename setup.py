from setuptools import setup

setup(
    name="scheduler",
    version='0.1.0',
    packages=[
        'scheduler',
        'scheduler.commands',
        'scheduler.providers'
    ],
    install_requires=[],
    include_package_data=True,
)
