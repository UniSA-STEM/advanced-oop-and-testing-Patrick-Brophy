import pytest
from staff import Staff, staff_register

class TestStaff:
    def __init__(self, staff_id, first_name, last_name, occupation):
        self._staff_id = staff_id
        self._first_name = first_name
        self._last_name = last_name
        self._occupation = occupation

    def get_staff_id(self): return self._staff_id
    def get_first_name(self): return self._first_name
    def get_full_name(self): return f"{self._last_name}, {self._first_name}"
    def get_occupation(self): return self._occupation

def test_create_zookeeper_staff(monkeypatch):
    """Testing the create staff function by creating a zookeeper staff."""
    inputs = iter(['jane', 'doe', 'Zookeeper', '50000'])
    monkeypatch.setattr('builtins.input', lambda x: next(inputs))
    expected_output = ("Jane Doe the Zookeeper has been created.\n"
                       "Jane can now be assigned a schedule and tasks related to their role.")

    result = Staff.create_staff()
    assert result == expected_output

def test_create_vet_staff(monkeypatch):
    """Testing the create staff function by creating a vet staff."""
    inputs = iter(['john', 'doe', 'Vet', '75000'])
    monkeypatch.setattr('builtins.input', lambda x: next(inputs))
    expected_output = ("John Doe the Vet has been created.\n"
                       "John can now be assigned a schedule and tasks related to their role.")
    result = Staff.create_staff()
    assert result == expected_output

@pytest.fixture
def test_synthetic_staff_register(monkeypatch):
    """Pre filled staff register function. Set as a fixture so staff objects are created by default."""
    staff_register.clear()
    staff_register['Staff_1'] = TestStaff('Staff_1', 'John', 'Doe', 'Zookeeper')
    staff_register['Staff_2'] = TestStaff('Staff_2', 'Jane', 'Deer', 'Vet')
    monkeypatch.setattr(Staff, 'get_staff_details', lambda: 'Mock Staff Details List')
    return staff_register

def test_staff_remove(monkeypatch, test_synthetic_staff_register):
    """Testing the staff removal function."""
    staff_id = 'Staff_1'
    inputs = iter([staff_id, 'y'])
    monkeypatch.setattr('builtins.input', lambda x: next(inputs))
    assert staff_id in staff_register
    expected_output = (f"You have removed {staff_id}.")
    result = Staff.remove_staff()
    assert result == expected_output
    assert staff_id not in staff_register
    assert 'Staff_2' in staff_register