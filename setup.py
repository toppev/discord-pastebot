import setuptools


setuptools.setup(
    name="discord-pastebot",
    version="0.1",
    description="Discord bot that creates pastebin pastes of long messages",
    long_description=open("README.rst").read(),
    
    url="https://github.com/toppev/discord-pastebot",
    author="Toppe",
    
    packages=setuptools.find_packages(),
    
    install_requires=[
        "discord.py>=0.16.12"
    ],
    
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Topic :: Communications :: Chat",
        "Framework :: AsyncIO",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
        
)