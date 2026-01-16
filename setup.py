from setuptools import setup, find_packages

setup(
    name="stoon",
    version="1.0.0",
    description="The S-TOON Protocol: Middleware for neutralizing structural injection in LLMs.",
    author="Jamil Alshaer",
    author_email="Azimuth-Logic-Research@proton.me",
    url="https://github.com/YOUR_USERNAME/S-TOON",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)