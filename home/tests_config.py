import pytest
from django.contrib.auth.models import User, Group

from home.models import UserAdditionalInfo

@pytest.fixture
def technician():
    tech = User.objects.create_user(
        username='kowalski_ada',
        first_name='Adam',
        last_name='Kowalski',
        email='adam.kowalski@lab.com',
        password='kowalski123!'
    )
    UserAdditionalInfo.objects.create(
        user=tech,
        phone_number='500500500',
        company='Strabag Sp. z o.o.'
    )
    technician_group, created = Group.objects.get_or_create(name='Technician')
    tech.groups.add(technician_group)
    return tech
