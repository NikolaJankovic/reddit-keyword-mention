import praw
from pprint import pprint

r = praw.Reddit(user_agent='python-flask-mention bot by /u/nikojanko')
r.login('novicenoobie', 'sendme')
posts = r.get_subreddit('python').get_hot(limit=25)
posts_compiled = ""

for x in posts:
    if 'flask' in str(x).lower():
        posts_compiled += "[{}]({})\n\n".format(str(x), str(x.permalink))

if len(posts_compiled) > 0:
    r.send_message('nikojanko', 'New Mention of Flask',
                   'There has been a mention of flask on /r/python: \n\n {}'.format(posts_compiled))
