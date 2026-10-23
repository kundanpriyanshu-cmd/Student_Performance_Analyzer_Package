""" 

Package Setup and Distribution Metadata for Student Performance Analyzer 

Allows local installation and distribution of the 'performance_analyzer' package. 

""" 

 

from pathlib import Path

from setuptools import find_packages, setup

ROOT = Path(__file__).resolve().parent
README_PATH = ROOT / "README.md"
if not README_PATH.exists():
    README_PATH = ROOT / "readme.md"

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

        "License :: OSI Approved :: MIT License", 

        "Operating System :: OS Independent", 

        "Topic :: Education", 

        "Topic :: Software Development :: Libraries :: Python Modules", 

    ], 

     

    # Dependencies (if any external packages are needed in the future) 

    install_requires=[ 

        # e.g., 'pytest>=7.0.0' for unit testing 

    ], 

) 