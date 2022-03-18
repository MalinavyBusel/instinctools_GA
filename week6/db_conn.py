from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from instinctools_GA.week6.table_creator import Post

DATABASE = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'mypassword)',
    'database': 'calculations'
}


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
    if oper and lim:
        return session.query(Post).filter(Post.operator == oper).limit(lim).offset(offs).all()
    elif lim:
        return session.query(Post).filter().limit(lim).offset(offs).all()
    elif oper:
        return session.query(Post).filter(Post.operator == oper).offset(offs).all()
    else:
        return session.query(Post).filter().offset(offs).all()


# smth = 0
# session = connect_to_db()
# for post in session.query(Post).filter().all():
#     print(post.operator, post.result)
# Post.id >= 1 if not smth else Post.operator == smth
