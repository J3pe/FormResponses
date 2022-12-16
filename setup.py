from setuptools import setup, find_packages


VERSION = '0.1.2'
DESCRIPTION = 'Send Google Forms responses using Python'
LONG_DESCRIPTION = 'A package that allows for sending Google Forms responses without even opening a browser.\nSee https://github.com/J3pe/googleforms for more information.'

# Setting up
setup(
    name="formresponses",
    version=VERSION,
    author="J3pe",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'requests', 'google', 'forms', 'form'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)