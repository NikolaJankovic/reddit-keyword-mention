# Reddit Keyword Mention

Simple bot to message a user on mention of a keyword in a subreddit. Checks every hour using a cron job, stores submission ID in an sqlite3 db that it parses prior to sending message to prevent duplicate messages containing the same link/submission.

