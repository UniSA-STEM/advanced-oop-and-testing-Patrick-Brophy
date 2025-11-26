import pytest
from enclosure import Enclosure, enclosure_register

@pytest.fixture
def occupied_enclosures():
    e1 = Enclosure(biome = 'Woods', size = 100)
    e1.set_is_clean()
    e2 = Enclosure(biome = 'Savannah', size = 200)
    e2.set_is_clean()
    e2.set_is_clean()
    e3 = Enclosure(biome = 'Alpine', size = 175)
    e3.set_occupancy('Animal_1')
    return {'Enclosure_1': e1, 'Enclosure_2': e2, 'Enclosure_3': e3}

def test_get_dirty_enclosures(occupied_enclosures):
    dirty_list = Enclosure.get_dirty_enclosures()
    assert dirty_list == ['Enclosure_1']
    assert ['Enclosure_2', 'Enclosure_3'] not in dirty_list

def test_set_is_clean(occupied_enclosures):
    e1 = occupied_enclosures['Enclosure_1']
    assert e1.get_is_clean() is False
    e1.set_is_clean()
    assert e1.get_is_clean() is True
    e1.set_is_clean()
    assert e1.get_is_clean() is False

def test_enclosure_search(monkeypatch, occupied_enclosures):
    inputs_id = iter(['Enclosure_3'])
    monkeypatch.setattr('builtins.input', lambda x: next(inputs_id))
    expected_output = ("The following enclosures matching 'Enclosure_3' were found:\n "
                       "Enclosure_3 of the Alpine biome is currently occupied by Animal_1 and is dirty")
    assert Enclosure.enclosure_search() == expected_output

