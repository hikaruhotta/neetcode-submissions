import heapq

class Twitter:

    def __init__(self):
        self.followees = {}
        self.tweets = {}
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = [followeeId for followeeId in self.followees[userId]] if userId in self.followees else []
        userIds = follows + [userId]

        tweets = {
            userId: self.tweets[userId]
            for userId in userIds if userId in self.tweets
        }

        max_heap = []
        for userId, posts in tweets.items():
            if len(posts) > 0:
                tweetId, timestamp = posts[-1]
                max_heap.append((-timestamp, tweetId, userId, len(posts) - 2))

        heapq.heapify(max_heap)

        newsfeed = []

        for i in range(10):
            if len(max_heap) > 0:
                timestamp, tweetId, userId, index = heapq.heappop(max_heap)
                newsfeed.append(tweetId)

                if index >= 0:
                    tweetId, timestamp = tweets[userId][index]
                    heapq.heappush(
                        max_heap,
                        (-timestamp, tweetId, userId, index - 1)
                    )

        return newsfeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followees:
            self.followees[followerId] = {}
        self.followees[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followees:
            self.followees[followerId] = {}
        if followeeId in self.followees[followerId]:
            del self.followees[followerId][followeeId]

        
