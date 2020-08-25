import setuptools

setuptools.setup(
    name="bric-layer",
    version="0.0.2",
    author="G B",
    description="Layer",
    long_description_content_type="text/markdown",
    url="https://github.com/bankova-gabriella/layer/",
    packages=["bric-layer"],
    install_requires=[
        "numpy",
        "pandas",
        "munch",
        "docker",
        "colorlog",
        "pipey",
        "graphene"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

# python setup.py sdist & twine upload --repository pypi dist/*
