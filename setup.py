import setuptools, os

if os.path.exists(os.path.join(os.getcwd(), README.md)):
    with open("README.md", "r") as f:
        long_description = f.read()    else:
    long_description = 'kksh'

setuptools.setup(
    name="kksh",
    version="0.0.1",
    author="Kristof",
    description="some shell functions for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/pysh",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)