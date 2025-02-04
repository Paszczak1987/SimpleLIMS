import pytest
from django.contrib.auth.models import Group

from home.models import Technician, Manager

@pytest.fixture
def technician():
    Group.objects.get_or_create(name='Technician')
    tech = Technician.objects.create(
        username="testerski_kar",
        first_name="Karol",
        last_name="Testerski",
        email="karol.testerski@bud.com",
        password="testerski_123",
        phone_number="505404101",
        company="Budobud",
    )
    return tech

@pytest.fixture
def manager():
    Group.objects.get_or_create(name='Manager')
    manager = Manager.objects.create(
        username="tester_art",
        first_name="Artur",
        last_name="Tester",
        email="artur.tester@lab.com",
        password="tester_123",
        phone_number="506405102",
        company="Labolab",
    )
    return manager
