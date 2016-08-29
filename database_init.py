import sqlite3

# database configuration
sqlite_file = 'db.sqlite'
table = 'posts'
col = 'post_id'
field_type = 'VARCHAR'

# Connecting to database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating new SQLite table
c.execute('CREATE TABLE {} ({} {})'.format(table, col, field_type))

conn.commit()
conn.close()
