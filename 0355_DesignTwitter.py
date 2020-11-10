from datetime import datetime
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follows = defaultdict(list) # user : follows id list
        self.tweets = defaultdict(list)  # user : tweets id list
        self.ttimes = {}  # tweet id : epoch time
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append(tweetId)
        dt = datetime.now()
        self.ttimes[tweetId] = dt.microsecond

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        # first collect followed users
        all_users = self.follows[userId] + [userId]
        # aggregate tweets of all_users
        all_tweets = []
        for uid in all_users:
            all_tweets += self.tweets[uid]
        
        tweets_time = []
        for tid in set(all_tweets):
            tweets_time.append((tid, self.ttimes[tid]))
        tweets_time.sort(key=lambda x: -x[1])
        feeds = []
        n = min(10, len(tweets_time))
        for i in range(n):
            feeds.append(tweets_time[i][0])
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
