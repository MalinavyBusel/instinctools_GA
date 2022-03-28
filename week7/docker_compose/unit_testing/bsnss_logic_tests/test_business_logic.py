from sqlalchemy.engine.url import URL
from sqlalchemy_utils.functions import database_exists
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from calculations import calculate

from testing_config import settings, Post


def test_connection():
    assert database_exists(URL.create(**settings.DATABASE)) == 1, 'Error in connection with database'


def connect():
    engine = create_engine(URL.create(**settings.DATABASE))
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


session = connect()
new_post = Post(operator='add',
                number1=5,
                number2=5,
                result=10.0)


def test_db_adding(session=session):
    session.add(new_post)
    session.commit()


def test_db_getting(session=session):
    query = session.query(Post).filter(Post == new_post).one()
    assert query, 'Check test1. If db is active, then smth with adding data went wrong.'
    if query:
        session.delete(new_post)
        session.commit()


session.close()


def test_operation():
    res, error = calculate('add 3 3').split(':::')
    assert res == '6'


def test_zero_division():
    res, error = calculate('truediv 3 0').split(':::')
    assert error == 'You are trying to divide by zero.'


def test_invalid_operator():
    res, error = calculate('multiply 3 3').split(':::')
    assert error == 'There is no such operation.'


def test_invalid_value():
    res, error = calculate('add a b').split(':::')
    assert error == 'Invalid arguments or their types.'
