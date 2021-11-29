# Political Bots for Representative Katie Porter

## My Favorite Interaction
I created five different bots to spread propaganda about my own district's (CA45) House representative, Katie Porter. Running the bot gave me outputs like [this](https://www.reddit.com/r/BotTown2/comments/r2rc5m/comment/hm6w096/?utm_source=share&utm_medium=web2x&context=3): 

![My Favorite Interaction](https://github.com/shreyachatterjee22/KatiePorterRedditBot/blob/main/favoriteinteractionscreenshot.JPG)

This is my favorite interaction because its just so random. None of the comments are remotely related to each other. The content goes from social to political to academic to political again. 

## My Bot Outputs
Below is the [output](https://github.com/shreyachatterjee22/KatiePorterRedditBot/blob/main/1000%20valid%20comments%20screenshot.JPG) from running bot_counter.py for my KatiePorterBot account located in bot1.py.

        len(comments)= 1000
        len(top_level_comments)= 240
        len(replies)= 760
        len(valid_top_level_comments)= 240
        len(not_self_replies)= 760
        len(valid_replies)= 760
        ========================================
        valid_comments= 1000
        ========================================
        NOTE: the number valid_comments is what will be used to determine your extra credit

I also ran 4 additional bots. Here are the outputs for those as well

bot2.py gives this output:

        len(comments)= 513
        len(top_level_comments)= 297
        len(replies)= 216
        len(valid_top_level_comments)= 293
        len(not_self_replies)= 216
        len(valid_replies)= 216
        ========================================
        valid_comments= 509
        ========================================
        NOTE: the number valid_comments is what will be used to determine your extra credit

bot3.py gives this output:

        len(comments)= 510
        len(top_level_comments)= 464
        len(replies)= 46
        len(valid_top_level_comments)= 464
        len(not_self_replies)= 46
        len(valid_replies)= 46
        ========================================
        valid_comments= 510
        ========================================
        NOTE: the number valid_comments is what will be used to determine your extra credit

bot4.py gives this output:

        len(comments)= 504
        len(top_level_comments)= 442
        len(replies)= 62
        len(valid_top_level_comments)= 442
        len(not_self_replies)= 62
        len(valid_replies)= 62
        ========================================
        valid_comments= 504
        ========================================
        NOTE: the number valid_comments is what will be used to determine your extra credit

bot5.py gives this output:

        len(comments)= 506
        len(top_level_comments)= 445
        len(replies)= 61
        len(valid_top_level_comments)= 445
        len(not_self_replies)= 61
        len(valid_replies)= 61
        ========================================
        valid_comments= 506
        ========================================
        NOTE: the number valid_comments is what will be used to determine your extra credit

## Upvotes and Downvotes
I also created a file which would upvote all mentions of biden and harris and downvote all mentions of trump and musk. Here is the output of running that file: 

![Up/Downvote Counts](https://github.com/shreyachatterjee22/KatiePorterRedditBot/blob/main/up_downvotes%20screenshot.JPG)

The first number represents how many comments were upvoted <br>
The second number represents how many comments were downvoted <br>
The third number represents how many submissions were upvoted <br>
The fourth number represents how many submissions were downvoted <br>

I ran this file until it hit over 100 submission votes and 500 comment votes in the BotTown2 Subreddit. I reached both the submission and comment up/downvote bar and so completed the task.

## Calculating Points

I completed the following tasks: 

Completing bot.py tasks = 18 points <br>
Completing github repo = 2 points <br>
Getting at least 100 valid comments posted = 2 points <br>
Getting at least 500 valid comments posted = 2 points <br>
Getting at least 1000 valid comments posted = 2 points <br>
Create an "army" of 5 bots w/500 valid comments = 2 points <br>
Up/Downvote comment or submission for candidates = 2 points <br>
Up/Downvote using TextBlob sentiment analysis = 2 points <br>

**Total Points Earned = 32 points**

## Some Notes

Interestingly, over the two weeks that I worked on this assignment I began to get targeted ads from Katie Porter's campaign spreading the news that she was supporting the Build Back Better Bill from the Democrats. I used my school email account for the inital reddit account and burner emails with the rest of the bots so I'm surprised that Google was still able to link the bot activity to my personal Google/Youtube account. 

I also wanted to note that before the original BotTown subreddit got deleted, I had reached around 800 comments. Having to rerun my first bot definitely set me back a lot but I was able to solve the issue with constant running and monitoring of my five files over the break. 

Finally, the link to the instructions for the project are [here](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_04).
