import os


def testing_migrations():
    migrations_result = os.system("alembic upgrade head")
    assert migrations_result == 0, 'The applying of migrations failed'
