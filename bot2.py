import praw
import random
import datetime
import time

# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "[PERSON] is a [GREAT] [NOUN].  She [CAN_DO] any [POLICY] faster than [OTHER]. [EVERYONE] [SHOULD] [VOTE] [PRONOUN].",
    "I [LOVE] [PERSON]! [EVERYONE] [SHOULD] [VOTE] [PRONOUN].",
    "[ENEMY] is  [BAD] and should be [REPLACE] by [PERSON]. [EVERYONE] with [SENSE] agrees.",
    "Ok but can [WE] all agree that [PERSON] is so much [BETTER] than [ENEMY]? You've got to [VOTE] her so she [CAN_DO] [POLICY].",
    "[WE] [SHOULD] all [LOVE] [PERSON] because [PRONOUN] [CAN_DO] [GREAT] [POLICY]. No [NOUN] is greater than her.",
    "If you really believe [ENEMY] is [BAD], then your vote for [PERSON] [CAN_DO] [GREAT] [THINGS]! Voting is so important!"
    ]

replacements = {
    'PERSON' : ['Porter', 'Katie Porter', 'CA Rep 45', 'Katie Porter, UCI Law professor turned House representative,','Porter, advocate for the middle class,'],
    'GREAT' : ['great', 'magnificent', 'fantastic', 'wonderful','exceptional','terrific', 'wonderful'],
    'NOUN' : ['person', 'leader', 'indivual','human','Congressperson','woman','force','representative'],
    'CAN_DO' : ['can do', 'is able to do', 'accomplishes','achieves','effects','effectuatues','implements'],
    'POLICY'  : [' policy', 'goals', 'things','objectives','missions','resolutions'],
    'OTHER' : ['anyone', 'the rest', 'others','any representative','other Congresspeople','her colleagues','both Democrats and Republicans'],
    'EVERYONE' : ['Everyone', 'Everyone (even republicans)', 'Everyone in her district', 'All residents of CA 45', 'People everywhere', 'You','Her constituents','Your family and friends'],
    'SHOULD' : ['should', 'must', 'need to','has an obligation to','has got to','ought to','will'],
    'VOTE' : ['vote for', 'support', 'fund','back','approve of','be supportive of'],
    'PRONOUN' : ['her', 'her candicacy', 'her campaign', 'her agenda','her policies','her ideas'],
    'LOVE' : ['love', 'adore', 'like'],
    'ENEMY' : ['Mitch McConnell', 'Ted Cruz', 'Kevin McCarthy', 'Nancy Pelosi','Matt Gaetz','Marjorie Taylor Greene'],
    'BAD' : ['the worst', 'appalling', 'a failure', 'not a patriot','stupid','a disaster'],
    'REPLACE' : ['replaced', 'destroyed', 'wrecked', 'torn down','usurped by'],
    'WE' : ['We','Our country','This group','We, as a collective,'],
    'BETTER' : ['better','more trustworthy','nicer','more approachable','more human','smarter','worthier','more knowledgable'],
    'THINGS' : ['things','goals','change','national impact','local impact'],
    'SENSE' : ['common sense','sense','a clue','critical thinking skills','any political savvy']

    }

def generate_comment():
    s=random.choice(madlibs)
    for k in replacements.keys():
        s=s.replace('['+k+']',random.choice(replacements[k]))
    return s


# connect to reddit 
reddit = praw.Reddit('KatiePorterBot2CA45')
print('reddit = ', reddit)


# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r3ipmj/starbucks_launches_aggressive_antiunion_effort_as/'
submission = reddit.submission(url=submission_url)

while True:
    # priNting the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # task 0: get a list of all of the comments in the submission
    submission.comments.replace_more(limit=None)
    all_comments = []
    for comment in submission.comments.list():
        all_comments.append(comment)
    print('len(all_comments)=',len(all_comments))

    # task 1: filter all_comments to remove comments that were generated by your bot
    not_my_comments = []
    for comment in submission.comments.list():
        if str(comment.author) != 'KatiePorterBot2':
            not_my_comments.append(comment)
    print('len(not_my_comments)=',len(not_my_comments))


    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented =',has_not_commented)
    if has_not_commented:
        # task 2: if you have not made any comment in the thread, then post a top level comment
        text = generate_comment()
        submission.reply(text)
        print('top level comment posted!')
    else:
        # task 3: filter the not_my_comments list to also remove comments that you've already replied to
        comments_without_replies = []
        for comment in not_my_comments:
            if comment.author != 'KatiePorterBot2':
                posted=False
                for replies in comment.replies:
                    if str(replies.author) == 'KatiePorterBot2':
                        posted=True
                if posted == False:
                    comments_without_replies.append(comment)
        print('len(comments_without_replies)=',len(comments_without_replies))

        # task 4: randomly select a comment from the comments_without_replies list, and reply to that comment
        for comments in comments_without_replies:
            selection = random.choice(comments_without_replies)
            try:
                selection.reply(generate_comment())
                print('reply posted!')
            except praw.exceptions.APIException:
                print('not replying to a comment that has been deleted')
            break



    # task 5: select a new submission for the next iteration; randomnumber = random.random()
    subreddit = reddit.subreddit("BotTown2")
    list_subreddit = list(subreddit.hot(limit=5))
    submission=random.choice(list_subreddit)

    # We sleep  for 5 seconds at the end of the while loop.
    time.sleep(15)