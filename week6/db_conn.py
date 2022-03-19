from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from instinctools_GA.week6.table_creator import Post
from instinctools_GA.week5.config import settings


DATABASE = settings.DATABASE


def connect_to_db(db_data: dict = DATABASE) -> 'Session':
    engine = create_engine(URL.create(**db_data))
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def add_data(session: 'Session', expression: str, res: float):
    try:
        oper, val1, val2 = expression.strip().split(' ')
        val1, val2 = float(val1), float(val2)
    except ValueError:
        return None
    new_post = Post(operator=oper,
                    number1=val1,
                    number2=val2,
                    result=res)
    session.add(new_post)
    session.commit()
    return None


def get_data(session: 'Session', oper: str, limit: str, offset: str):
    offs = int(offset) if offset else 0
    lim = int(limit) if limit else 0
    query = session.query(Post).offset(offs)
    if lim:
        query = query.limit(lim)
    if oper:
        query = query.filter(Post.operator == oper)
    return query.all()
