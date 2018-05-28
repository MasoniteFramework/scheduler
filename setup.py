from setuptools import setup

setup(
    name="scheduler",
    version='0.0.1',
    packages=[
        'scheduler',
        'scheduler.commands',
        'scheduler.providers'
    ],
    install_requires=[],
    include_package_data=True,
)
