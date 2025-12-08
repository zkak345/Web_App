# Web_App
This ReadMe will cover the documentation for this project.

# Executive Summary
Cargo2Go is a web application where managers can access a simple yet easy to use web interface to manage cargo shipments between warehouse, vendors, and customers. Cargo2Go will feature a dashboard that will allow managers to track package details, locations, history, delivery status.
Each shipment that can be managed will include a tracking ID, delivery info, status, timestamps, entries, and more. Cargo2Go is meant to provide a simple means to manage shipments and ensure all is running smoothly.

# AI Disclaimer
This project used AI in certain areas such as template generation, and help with functionality
## Installation
Clone the repository
```bash
git clone repo.git
```
Switch into the correct folder
```bash
cd Web_App/cargo2go

```

Create a virtual environment (optional)
```
python -m venv venv
venv/Script/activate (if on windows)
```

Install requirements
```
pip install -r requirement.txt
```


Build the docker image
```
docker-build .
docker-compose run django bash
```

Make changes and migrate
```bash
python manage.py migrate
```

Create Admin
```
python manage.py createsuperuser
```

## Getting Started
Start up the app
``` bash
docker-compose up

```

Login with admin at /admin

Enjoy!



# License

Zaid Kakish
