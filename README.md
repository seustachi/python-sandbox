# Only the first time, to create the virtual environment
py -m venv banking_env

# From git bash, this activates the virtual environment
source ./banking_env/Scripts/activate

# Checking how I can call pip with this venv  
py -m pip --version

# installing some stuff
py -m pip install numpy
