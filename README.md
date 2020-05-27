# PictureSplash

# Author
Khadija Hassan

# Description
This a Django application which allow a user to create and upload an image and can also copy the link of the image

# User Stories
* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo
* Search for different categories of photos
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

# Setup Instaltion

github clone:
```bash
https://github.com/khadija-bit/PictureSplash.git
```

Navigate to the directory:
```bash
cd PictureSplash
```

Installation requirements:
```bash
pip freeze > requirements.txt
```

Install Django
```bash

pip install django==1.11
```

Database Migration:

run check
```bash
python3.6 manage.py check
```

Make Migration
'''bash
python manage.py makemigrations < project app name>
```

Migrate
```bash
python3.6 manage.py migrate
```

Run application
```bash
python3.6 manage.py runserver
```

# Technology Used
* Bootstrap
* Python3.6
* CSS
*
* Django 1.11
* Heroku
