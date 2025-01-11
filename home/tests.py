import pytest
from django.test import Client
from django.urls import reverse
from home.tests_config import technician


# Create your tests here.

@pytest.mark.django_db
def test_login(technician):
    client = Client()
    client.force_login(technician)
    url = reverse('home:login')
    response = client.get(url)
    assert response.status_code == 200
    