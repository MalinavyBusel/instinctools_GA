import psycopg2

from sqlalchemy import text

from instinctools_GA.week6.table_creator import Post
from instinctools_GA.week5.config import settings


DATABASE = settings.DATABASE
conn = psycopg2.connect(**DATABASE)
cur = conn.cursor()

# 1
cur.execute("SELECT * FROM operations WHERE result<%(res)s", {'res': 0})

# 2
cur.execute("SELECT COUNT(*) FROM operations WHERE result<%s", (0, ))

# 3
cur.execute('''SELECT operator, COUNT(operator)
FROM operations
GROUP BY operator''')

# 4
cur.execute('''SELECT operator, CAST(COUNT(operator)/(SELECT COUNT(*) FROM operations)*100 AS INT)
FROM operations
GROUP BY operator''')

# 5
cur.execute('''SELECT operator, SUM(dupl) AS duplicated_count
FROM (SELECT operator, number1, number2, COUNT(id)-1 as dupl, COUNT(id) AS total
FROM operations
GROUP BY operator, number1, number2) AS tab1
GROUP BY operator
UNION 
SELECT COUNT(*) as unique_count
FROM (SELECT operator, number1, number2, COUNT(id)
FROM operations
GROUP BY operator, number1, number2
HAVING COUNT(id) =1) AS tab1
GROUP BY operator''')

# Here is a variant of raw request using SQLAlchemy. Is it also correct?
my_request = '''SELECT operator, COUNT(operator)
FROM operations
GROUP BY operator'''
query = session.query(Post).filter(text(my_request)).all()
