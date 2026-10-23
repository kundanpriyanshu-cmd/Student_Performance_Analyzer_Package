# Student Performance Analyzer (`performance_analyzer`) 

 

A modular, production-grade Python package for score input validation, automated grading rules, and class performance analytics. Built as part of **Industry Skill Studio 03** (*Python Programming & Software Automation - Y1UD102B*). 

 

--- 

 

## 📌 Project Overview 

 

The `performance_analyzer` package transitions software development away from monolithic scripts by organizing business logic into clean, reusable modules. It provides defensive validation gates for student marks and computes aggregate class statistics with robust error handling. 

 

--- 

 

## 📁 Project Architecture 

 

```text 

student_analyzer_project/ 

│ 

├── performance_analyzer/             <-- CUSTOM PYTHON PACKAGE 

│   ├── __init__.py                   <-- Package Initializer & Namespace Exports 

│   ├── validator.py                  <-- Sub-Module 1: Input Validation Engine 

│   └── metrics.py                    <-- Sub-Module 2: Grading & Class Analytics 

│ 

├── main.py                           <-- Driver Application (Package Consumer) 

└── setup.py                          <-- Package Setup & Distribution Metadata 
```