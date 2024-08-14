# Pip lets you install packages that are not included in python.

# open your terminal and type in $ " pip install " --> today I'm working with "requests" so it'll look like $ "python3 -m pip install requests" because Im working on a macos but on windows it would be $ "py -m pip install requests". (Do not use "" in terminal)

# you can view everything you've install in pip using
#
# $ python3 -m pip list

# to install a specific version of a python package use for example:
# $ "python3 -m pip install requests==2.30.0"

# to upgrade a package in python use for example:
# $ "python3 -m pip install -U requests"

# this will upgrade it to the most updated version of that package release.

# to Uninstall a python package for example:
# $ "python3 -m pip uninstall requests"

###################################################################

# There will be times where you will need to work in a virtual environment.

# you will have to use
# $ python3 -m venv [.insert_name]

# activate the folder
# $ source .venv/bin/activate <--- for macOS users
# $ source .venv/Scripts/activate <--- for windows users

# to deactivate the Virtual Environment type
# $ deactivate

# there is a website to use when looking to install python packages it is

# pypi.org


# Do not upload your virtual environment to Github repo. use:

# $ python3 -m pip freeze > requirements.txt

# make a new file called:

# .gitignore
# inside that file you are going to type .venv and save the file.
