from setuptools import setup, find_packages

setup(
    name="nglstrike",
    version="1.2.0",
    author="Mallik Mohammed Musaddiq",
    author_email="mallikmusaddiq1@gmail.com",
    description="Anonymous Auto-Sender for NGL",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="."),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "nglstrike = nglstrike.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)