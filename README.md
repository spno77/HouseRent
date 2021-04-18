# HouseRent
An airbnb-like site build with Django (Django REST Framework) + Vue (BootstrapVue + Vue Router + Vuex).


### Installation

### Back end

**Create virtual env**
> python3 -m venv env	

**Activate the virtual env**
> source env/bin/activate

**Install dependencies**
> pip install -r requirements.txt

**Apply all migrations**
> ./manage.py migrate

**Create Admin**
> ./manage.py createsuperuser

**Run it**
> ./manage.py runserver_plus --cert-file cert.crt

### Front end

**Install dependencies**
> npm i @vue/cli-service

**Run**
> npm run serve

### Examples:

### Make a reservation

![reserve](https://github.com/spno77/HouseRent/blob/master/backend/media/reserve.gif)