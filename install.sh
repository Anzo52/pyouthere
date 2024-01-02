#!/bin/bash


# define the name of virtual environment
# TODO: make this a command line argument
VENV_DIR="env"

# check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR

fi

# activate virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# notify if virtual environment is or is not activated, if not, notify user to activate it and exit
if [ -z ${VIRTUAL_ENV+x} ]; then
    echo "Virtual environment is not activated."
    echo "Please activate virtual environment and run this script again."
    exit 1
else
    echo "Virtual environment is activated."
fi

# install dependencies
# leave as is if you are using setup.py
# if you are using requirements.txt, comment out and uncomment the respective lines marked with a comment "#"
echo "Installing dependencies..."
python3 setup.py install  # comment out if using requirements.txt
# pip3 install -r requirements.txt # uncomment if using requirements.txt

echo "Installation complete, run 'pyou' or './pyou' to start the program. Don't forget to deactivate the virtual environment when you are done."


