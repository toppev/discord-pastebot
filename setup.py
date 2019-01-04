import setuptools

setuptools.setup(
    name="discord-pastebot",
    version="0.1",
    description="Discord bot that creates pastebin pastes of long messages",
    long_description=open("README.md").read(),
    
    url="https://github.com/toppev/discord-pastebot",
    author="Toppe",
    
    packages=setuptools.find_packages(),
    
    install_requires=[
        "discord.py>=0.16.12"
    ],
    
    package_data={'': ['config.txt']},
    include_package_data=True,
    
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Communications :: Chat",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
        
)
