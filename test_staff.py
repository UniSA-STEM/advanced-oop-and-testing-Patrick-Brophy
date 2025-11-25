import pytest
from staff import *

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
