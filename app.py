import praw
import sqlite3

USERNAME = 'username'
PASSWORD = 'password'
USER_RECEIVE = 'receiving_user'
USER_AGENT = 'Subreddit Keywork Search v0.1 - /u/{}'.format(USERNAME)
SUBREDDIT = 'subreddit'
KEYWORD = 'keyword'

# Connecting to database file

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

# Bot Logic

r = praw.Reddit(user_agent=USER_AGENT)
r.login(USERNAME, PASSWORD, disable_warning=True)
posts = r.get_subreddit(SUBREDDIT).get_hot(limit=25)  # list of submissions
posts_compiled = ""  # string containing formatted submissions that contain 'flask'

for x in posts:
    if KEYWORD in str(x).lower():
        [[exists]] = c.execute('SELECT EXISTS(SELECT 1 FROM posts WHERE post_id=? LIMIT 1)', [x.id])
        if exists == 0:
            posts_compiled += "[{}]({})\n\n".format(str(x.title), str(x.permalink))
            c.execute('INSERT INTO posts(post_id) VALUES (?)', [x.id])
            conn.commit()

if len(posts_compiled) > 0:
    r.send_message(USER_RECEIVE, 'New Mention of {}'.format(KEYWORD),
                   'There has been a mention of {} on /r/{}: \n\n {}'.format(KEYWORD, SUBREDDIT, posts_compiled))

conn.commit()
conn.close()
