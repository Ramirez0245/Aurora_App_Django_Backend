pip install django djangorestframework python-dotenv psycopg2-binary

1. Activate Enviroment
2. $ mkdir Aurora_Backend_REST_API, then cd into it.
3. $ pip install django djangorestframework
4. $ django-adimin startproject config .
5. $ python manage.py startapp <test_app> // Makes App - 
6. $ django-admin startproject config . // Create mange.py, project folder (config/), settings files
7. $ python manage.py runserver // start server


======================== TESTING MYSQL BUILD =================
$ pip install mysqlclient

================== TESTING CRUD BUILD ================
backend/
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
└── manage.py

1. Include in settings.py
    'rest_framework',
    '<app_name>',
2. Include in models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
3. Run migration
python manage.py makemigrations
python manage.py migrate

4. Include Serializer (serializers.py) - Serializers convert model instances ↔ JSON.
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

5. Including Views (views.py)
from rest_framework.viewsets import ModelViewSet
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

6. Include URLs (<app_name>/urls.py)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]






========================= PROJECT EXAMPLE STRUCTURE ==================
Aurora_Backend_REST_API/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   └── settings/
│       ├── __init__.py
│       ├── base.py
│       ├── local.py
│       └── production.py
│
├── apps/
│   ├── users/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── services.py
│   │
│   ├── products/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── services.py
│
├── common/
│   ├── permissions.py
│   ├── pagination.py
│   ├── exceptions.py
│   └── utils.py
│
├── manage.py
├── requirements.txt
└── .env

High-Level Architecture 
Clients (React, Mobile, etc.)
        |
        |  HTTPS / JSON
        v
API Gateway / Load Balancer
        |
        v
Django REST API
        |
        v
Business Logic Layer
        |
        v
Database (PostgreSQL)

Key Design Principles:
- Domain-Driven App Structure
- Apps are organized by business domains, not by technical layers.

Good (production):
users/
products/
orders/
payments/
Each app owns its logic end-to-end.


Backend responsibility:
Data, business rules, authentication, permissions, integrations
This separation:
•	Enables multiple clients (web, mobile, IoT)
•	Improves scalability
•	Allows teams to work independently

