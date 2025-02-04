import pytest
from django.test import Client
from django.urls import reverse
from home.tests_config import technician, manager


# Create your tests here.

@pytest.mark.django_db
def test_technician_login(technician):
    client = Client()
    client.force_login(technician)
    url = reverse('home:login')
    response = client.get(url)
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_manager_login(manager):
    client = Client()
    client.force_login(manager)
    url = reverse('home:login')
    response = client.get(url)
    assert response.status_code == 200

