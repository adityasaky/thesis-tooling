from setuptools import setup, find_packages

long_description = "thesis-tooling"

setup(
    name="pacrank",
    version="0.1.0",
    author="Aditya Saky",
    author_email="aditya.sirish@nyu.edu",
    description=long_description,
    long_description=long_description,
    url="https://github.com/adityasaky/thesis-tooling",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "pacrank-rank = pacrank.pacrank_rank:main",
            "pacrank-display = pacrank.pacrank_display:main",
            "pacrank-analyse = pacrank.pacrank_analyse:main"
        ]
    }
)