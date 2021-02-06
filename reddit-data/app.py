import praw
import pandas as pd

posts = []

reddit = praw.Reddit(client_id='e6qeyZCLeP9IQQ', client_secret='l_6dsZYdeYXvvLuO4MZ1v2Sx-5w4Lw', user_agent='Reddit WebScraping')

# get all posts from the subreddit
sw_subreddit = reddit.subreddit('SuicideWatch').hot(limit=10)
for post in sw_subreddit:
    # Adding main thread details
    posts.append([post.title])
    
    # Handling replies
    submission = reddit.submission(url=post.url)
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        posts.append([comment.body])

posts = pd.DataFrame(posts,columns=['body'])
print(posts)

compression_opts = dict(method='zip', archive_name='out.csv')  
posts.to_csv('out.zip', index=False, compression=compression_opts)  