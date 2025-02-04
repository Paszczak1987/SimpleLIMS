import pytest
from django.contrib.auth.models import Group

from home.models import Manager
from laboratory.models import Laboratory


@pytest.mark.django_db
def test_laboratory_manager_assignment():
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
    lab = Laboratory.objects.create(
        name='BioTech Lab',
        short_name='BTL',
        code='BT001',
        street='Science Ave',
        number='10',
        city='Gdansk',
        postal_code='80-001',
        country='Poland',
        manager=manager
    )
    
    assert lab.manager == manager
    assert manager.laboratory == lab

