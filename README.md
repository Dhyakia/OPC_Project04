# OPC_Project04
Develop a program using Python : Chess tournaments manager


# Introduction -  What's torga ?

Torga is an offline program aimed at organising chess tournaments, following the Swiss rules. 
It feature a very basic set of functionnality such as :
* Customizing the number of rounds, duration, name ... of a tournament.
* Possibility to save and load a tournament.
* View on the database, table of all the players, tournaments and data inside tournaments.


# Requirements

* Python3 at https://www.python.org/downloads
* Pip at https://pip.pypa.io/en/stable/installing/ 

# Installation

## 1. Getting the code

Using the git tool or straight from the source

### Method git
```
mkdir mon_dossier
cd mon_dossier
git clone https://github.com/Dhyakia/OPC_Project04.git
```
### Method Manual
1. Go [here](https://github.com/Dhyakia/OPC_Project04)
2. Click on "Code" (green button) and then "Download Zip"
3. Un-zip the file and you're done !

## 2. Setting up a virtual environement
1. With the console command, navigate to the instalation folder
2. To create the virtual environement, enter this command :

   Windows : ```python3 -m venv c:\path\to\myenv```

   MacOs/Linux : ```python3 -m venv env```
3. Now that the virtual environoment is created, you need to activate it :

   Windows : ```cd myvenv/Scripts``` puis ```activate```
   
   MacOs/Linux : ```cd myvenv/bin``` puis ```activate```
   
4. You can now see the (venv) written at the very left of the line in the console command, signaling the success of the operation.

## 3. Module installation

1. Using the console, navigate where the file were un-zipped.
2. Enter this command :
```
pip install -r requirements.txt
```
Wait for all the modules to download and install.

# Usage

<b>WARNING :</b> Before starting the program, make sure your virtual environement is activated.

In the console, navigate to where torga.py is located en enter :
```
python torga.py
```
To save a tournament, type `save` when asked to enter a score. This will save the tournament for later.

# Generate a new flake8-html

To generate a new flake8 report, paste this line into your console :
```
flake8 --format=html --htmldir=flake8_rapport --max-line-length=119 --filename=*.py --exclude=.\venv\
```


# Futur viewing

This is the forth project out of the thirtheen python project.
Realised with OpenClassRoom, more to come in the year 2021.