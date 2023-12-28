# Overview

This is a collaborative effort to organize and catalog resources related to natural language processing of native languages of Sri Lanka - Tamil and Sinhala.  

# Contributing to this project

>[!NOTE]  
>Find more information on contributing resources to this documentation [here.](https://nlplk.github.io/contribute/)

Contributions to this project in terms of code are also welcome. For any code changes open a PR to the `master` branch with the relevant changes. Describe the changes made clearly in the PR description with screenshots if neccessary. 

For bugs and features open an issue with the relevant information. 

# Local setup

This documentation is built using [mkdocs](https://www.mkdocs.org/), more specifically [mkdocs-material](https://squidfunk.github.io/mkdocs-material/). mkdocs is static site generator that uses markdown source files. `mkdocs-material` is a framework built on top of mkdocs. This project needs `Python 3.10+` to be installed locally to carry out the development.   

Install and setup python locally. Use your os specific installation guide for python installation. Any python 3.10+ should support development. Find python binaries and installers [here.](https://www.python.org/downloads/)

>[!TIP]  
>Use a virtual environment like `venv` to set up the development environment. But it is not compulsory.  

install the required dependencies using `pip`:
```
pip install -r requirements.txt
```  

Install the custom `publications-sort` plugin:
```
pip install ./plugins/.
```  
To generate the static site files run:
```
mkdocs build
```
Mkdocs has a live preview server with hot reload capabilities to view changes made in real time. This live preview server can be started without running `mkdocs build`. Start a live preview server with:
```
mkdocs serve
```  
