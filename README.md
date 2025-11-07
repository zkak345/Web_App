# Web_App
This ReadMe will cover the documentation for this project.

# Executive Summary
Cargo2Go is a web application where managers can access a simple yet easy to use web interface to manage cargo shipments between warehouse, vendors, and customers. Cargo2Go will feature a dashboard that will allow managers to track package details, locations, history, delivery status.
Each shipment that can be managed will include a tracking ID, delivery info, status, timestamps, entries, and more. Cargo2Go is meant to provide a simple means to manage shipments and ensure all is running smoothly.

# # Installation
```bash
docker-build .
docker-compose run django bash
python manage.py migrate
python manage.py createsuperuser
```

# # Getting Started
``` bash
docker-compose up
```

