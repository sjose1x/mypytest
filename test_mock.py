import pytest
from mock import MagicMock
from mock_example import Person, DB

@pytest.fixture
def mock_db():
    return MagicMock(spec=DB)

def test_save_persist_to_db(mock_db):
    sashi = Person("Sashi", mock_db)
    sashi.save()
    mock_db.persist.assert_called_with(sashi)
    
def test_save_persist_to_db(mock_db):
    mock_db.persist.assert_called_with()
    
def test_called_with_other_agr(mock_db):
    mock_db.persist(1,2,3)
    mock_db.persist.assert_called_with()
    
def test_any_call_mock_db(mock_db):
    mock_db.persist(1)
    mock_db.persist(3)
    #assert_called_with() will check for the last call
    mock_db.persist.assert_any_call(1)