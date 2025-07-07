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


