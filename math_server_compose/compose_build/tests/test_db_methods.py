from sqlalchemy.engine.url import URL
from sqlalchemy_utils.functions import database_exists
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from calc_processing.config import settings
from calc_processing.data_models import Post


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
