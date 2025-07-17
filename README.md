# Only the first time, to create the virtual environment
py -m venv banking_env

# From git bash, this activates the virtual environment
source ./banking_env/Scripts/activate

# Checking how I can call pip with this venv 
py -m pip --version

# Installing some stuff
py -m pip install numpy

# Using numpy (should work!)
py ./dummy-numpy.py

# Deactivate the virtual env
deactivate

# Using numpy (should not work now !)
py ./dummy-numpy.py

# How to debug a file in python 
Just click on the debugbutton :D

# How to run a unit test ?




to go further, here is the proposed structure for a data analysis project : 

## Day 5 Solution Highlights:

**1. Complete Project Structure**
- Organized directory layout for data science projects
- Separation of raw vs processed data
- Dedicated folders for notebooks, source code, tests, and documentation

**2. Essential Project Files**
- `README.md` with clear setup instructions
- `requirements.txt` with all necessary data science packages
- `.gitignore` for Python and data science projects
- Configuration files for project settings

**3. Modular Code Structure**
- `DataLoader` class for handling data input/output
- `DataProcessor` class for data cleaning and transformation
- Proper Python package structure with `__init__.py` files

**4. Testing Framework**
- Unit tests using pytest
- Example tests for data loading functionality

**5. Jupyter Notebook Template**
- Ready-to-use notebook for data exploration
- Proper imports and project structure integration

**6. Virtual Environment Best Practices**
- Step-by-step instructions for environment setup
- Demonstration of package management concepts
- Common pip commands reference

This solution gives you a **production-ready template** for any data science project, with all the professional development practices that employers expect to see. You can use this structure as a starting point for all your future AI/ML projects!

The key takeaway from Day 5 is learning to set up **isolated, reproducible environments** - this is crucial when working with different AI/ML projects that may require different package versions.


