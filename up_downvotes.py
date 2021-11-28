import praw
import random
import time
from textblob import TextBlob

#connect to reddit
reddit = praw.Reddit('KatiePorterBotCA45')
print('reddit = ', reddit)

subreddit = reddit.subreddit("BotTown2")
list_subreddit = list(subreddit.hot(limit=None))

comment_upvotes = 0
comment_downvotes = 0
submission_upvotes = 0
submission_downvotes = 0
for submission in list_subreddit:
    print('new submission')
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        print('new comment')
        words = TextBlob(str(comment.body))
        polarity = words.sentiment.polarity
        opinion = words.sentiment.subjectivity
        #upvotes on comments
        print(comment.body)
        if 'biden' in comment.body.lower() and polarity > 0.5:
            comment.upvote()
            comment_upvotes +=1
            print('comment upvoted!')
        if 'harris' in comment.body.lower() and polarity > 0.5:
            comment.upvote()
            comment_upvotes +=1
            print('comment upvoted!')
        #downvotes on comments
        if 'trump' in comment.body.lower() and polarity > 0.5:
            comment.upvote()
            comment_downvotes +=1
            print('comment downvoted!')
        if 'musk' in comment.body.lower() and polarity > 0.5:
            comment.upvote()
            comment_downvotes +=1
            print('comment downvoted!')

    #upvotes on submissions
    if 'biden' in submission.title.lower():
        comment.upvote()
        submission_upvotes +=1
        print('thread upvoted!')
    if 'harris' in submission.title.lower():
        comment.upvote()
        submission_upvotes +=1
        print('thread upvoted!')
    #downvotes on submissions
    if 'trump' in submission.title.lower():
        comment.downvote()
        submission_downvotes +=1
        print('thread downvoted!')
    if 'musk' in submission.title.lower():
        comment.downvote()
        submission_downvotes +=1
        print('thread downvoted!')

    print(comment_upvotes)
    print(comment_downvotes)
    print(submission_upvotes)
    print(submission_downvotes)


    time.sleep(7)