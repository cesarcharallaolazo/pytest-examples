import pytest

from src.student import StudentDB


@pytest.fixture(scope="module")
def db():
    print('---setup---')
    db = StudentDB()
    db.connect('./src/data.json')
    yield db
    print('---teardown---')
    db.close()


def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'

## --------------------------------
# db = None
#
# def setup_module(module):
#     print('--setup---')
#     global db
#     db = StudentDB()
#     db.connect('data.json')
#
#
# def teardown_module(module):
#     print('--teardown---')
#     db.close()
#
#
# def test_scott_data():
#     scott_data = db.get_data('Scott')
#     assert scott_data['id'] == 1
#     assert scott_data['name'] == 'Scott'
#     assert scott_data['result'] == 'pass'
#
#
# def test_mark_data():
#     mark_data = db.get_data('Mark')
#     assert mark_data['id'] == 2
#     assert mark_data['name'] == 'Mark'
#     assert mark_data['result'] == 'fail'

## --------------------------------

# def test_scott_data():
#     db = StudentDB()
#     db.connect('data.json')
#     scott_data = db.get_data('Scott')
#     assert scott_data['id'] == 1
#     assert scott_data['name'] == 'Scott'
#     assert scott_data['result'] == 'pass'
#
#
# def test_mark_data():
#     db = StudentDB()
#     db.connect('data.json')
#     mark_data = db.get_data('Mark')
#     assert mark_data['id'] == 2
#     assert mark_data['name'] == 'Mark'
#     assert mark_data['result'] == 'fail'
