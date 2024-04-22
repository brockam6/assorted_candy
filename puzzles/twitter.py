"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

Input
    ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
    [null, null, [5], null, null, [6, 5], null, [5]]

Explanation
    Twitter twitter = new Twitter();
    twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2);    // User 1 follows user 2.
    twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.unfollow(1, 2);  // User 1 unfollows user 2.
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2
"""
class Twitter:

    def __init__(self):
        # Each tweet contains (tweetId, userId)
        self.tweet_count = 0
        self.tweets = []
        self.users = {}
        
    
    def _add_user(self, userId):
        self.users[userId] = User(userId)


    def _check_user_existence(self, *ids: int):
        for userId in ids:
            if userId in self.users:
                pass
            else:
                self._add_user(userId)
        return True


    def postTweet(self, userId: int, tweetId: int) -> None:
        """Tweet gets added to both the Twitter object and the users tweets.
            Both need to be in chronological order"""
        if self._check_user_existence(userId):
            self.users[userId].tweet(tweetId)

        self.tweet_count += 1
        heapq.heappush(self.tweets, (-self.tweet_count, -tweetId, userId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """Get the 10 most recent tweets. Cross check the tweet was created by the user, or
           someone the user follows and order the final list most -> least recent """
        feed = []
        skipped = []

        # Make copy of tweets so we don't transform the list during iterations
        copy_tweets = self.tweets.copy()

        # Go until we find 10 tweets matching the condition or run out of tweets
        for tw in copy_tweets:
            # Found 10 valid tweets for the feed. Add all skipped tweets back to the heap
            if len(feed) == 10:
                break
            # Pull the most recent tweet
            most_recent = heapq.heappop(self.tweets)
            # If current user made the tweet, add to feed
            if most_recent[2] == userId:
                heapq.heappush(feed, most_recent)
            # If a user the current user follows made the tweet, add to feed
            elif most_recent[2] in self.users[userId].follows:
                heapq.heappush(feed, most_recent)
            # The tweet should not be part of the users feed. Add to skipped
            else:
                heapq.heappush(skipped, most_recent)

        self.tweets = copy_tweets
        return [-x[1] for x in feed]


    def follow(self, followerId: int, followeeId: int) -> None:
        """Add the id of the followee to the followers follower attribute.
           Add the id of the follower to the followees follows attribute"""
        if self._check_user_existence(followerId, followeeId):
            self.users[followerId].follow_new(followeeId)
            self.users[followeeId].add_follower(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """Remove the id of the followee to the followers follower attribute.
           Remove the id of the follower to the followees follows attribute"""
        if self._check_user_existence(followerId, followeeId):
            self.users[followerId].unfollow(followeeId)
            self.users[followeeId].remove_follower(followerId)
        

class User:

    def __init__(self, user_id: int):
        self.user_id = user_id
        self.followers = {}
        self.follows = {}
        self.tweets = []

    def add_follower(self, follower_id):
        """Add a new follower to the user"""
        self.followers[follower_id] = True

    def remove_follower(self, follower_id):
        """Remove a follower from the user"""
        if follower_id in self.followers:
            del self.followers[follower_id]

    def follow_new(self, followee_id):
        """Add a new user to the accounts followed"""
        self.follows[followee_id] = True

    def unfollow(self, followee_id):
        """Remove a user from the accounts followed"""
        if followee_id in self.follows:
            del self.follows[followee_id]

    def tweet(self, tweetId: int):
        """Add a new tweet to the users active tweets"""
        heapq.heappush(self.tweets, tweetId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

