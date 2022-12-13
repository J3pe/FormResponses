from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Send Google Forms responses using Python'
LONG_DESCRIPTION = 'A package that allows for sending Google Forms responses without even opening a browser.'

# Setting up
setup(
    name="googleforms",
    version=VERSION,
    author="J3pe",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'requests', 'google', 'forms', 'form'],
    classifiers=[
        "Intended Audience :: Anyone",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)