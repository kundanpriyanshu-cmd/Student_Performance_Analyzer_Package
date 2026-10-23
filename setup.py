""" 

Package Setup and Distribution Metadata for Student Performance Analyzer 

Allows local installation and distribution of the 'performance_analyzer' package. 

""" 

 

import pathlib

try:
    from setuptools import find_packages, setup  # pyright: ignore[reportMissingModuleSource]
except ModuleNotFoundError as exc:
    raise RuntimeError(
        "setuptools is required to run setup.py directly. "
        "Prefer installing the package with `python -m pip install -e .` "
        "from the project directory."
    ) from exc

ROOT = pathlib.Path(__file__).resolve().parent


def find_readme() -> pathlib.Path:
    """Return the README file regardless of filename case."""
    for candidate in ROOT.iterdir():
        if candidate.is_file() and candidate.name.lower() == "readme.md":
            return candidate
    return ROOT / "readme.md"


README_PATH = find_readme()

setup(
    # Package Identification
    name="performance_analyzer",
    version="1.0.0",
    author="Educational Data Systems Team",
    author_email="devs@educationaldata.org",
    description="A modular Python package for score validation, grading rules, and class performance analytics.",

    # Detailed Description
    long_description=README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else "",
    long_description_content_type="text/markdown",

    # Package Discovery
    packages=find_packages(),  # Automatically discovers 'performance_analyzer'
     

    # Environment & Python Requirements 

    python_requires=">=3.8", 

     

    # Package Classification Metadata 

    classifiers=[ 

        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",

        "Topic :: Education", 

        "Topic :: Software Development :: Libraries :: Python Modules", 

    ], 

     

    # Dependencies (if any external packages are needed in the future) 

    install_requires=[ 

        # e.g., 'pytest>=7.0.0' for unit testing 

    ], 

) 