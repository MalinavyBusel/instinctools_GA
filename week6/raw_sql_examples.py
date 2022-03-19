import psycopg2

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
