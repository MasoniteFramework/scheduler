from setuptools import setup

setup(
    name="masonite-scheduler",
    version='1.0.2',
    package_dir={'': 'src'},
    packages=[
        'scheduler',
        'scheduler.commands',
        'scheduler.providers'
    ],
    author='Joe Mancuso',
    author_email='joe@masoniteproject.com',
    install_requires=[],
    include_package_data=True,
)
