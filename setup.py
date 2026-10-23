""" 

Package Setup and Distribution Metadata for Student Performance Analyzer 

Allows local installation and distribution of the 'performance_analyzer' package. 

""" 

 

from pathlib import Path

from setuptools import setup, find_packages 

 

setup( 

    # Package Identification 

    name="performance_analyzer", 

    version="1.0.0", 

    author="Educational Data Systems Team", 

    author_email="devs@educationaldata.org", 

    description="A modular Python package for score validation, grading rules, and class performance analytics.", 

     

    # Detailed Description
    long_description=(Path(__file__).parent / "readme.md").read_text(encoding="utf-8"),

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