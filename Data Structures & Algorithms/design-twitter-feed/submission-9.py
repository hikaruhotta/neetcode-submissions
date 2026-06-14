import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.follows = {}
        self.tweets = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = [userId]
        if userId in self.follows:
            for followeeId in self.follows[userId]:
                users.append(followeeId)

        tweet_indices = [-1] * len(users) 

        max_heap = []
        
        for i, user in enumerate(users):
            if user in self.tweets and len(self.tweets[user]) > 0:
                tweet_indices[i] = len(self.tweets[user]) - 1
                tweetId, time = self.tweets[user][-1]
                heapq.heappush(max_heap, (-time, tweetId, i))
        
        result = []

        while max_heap and len(result) < 10:
            time, tweetId, index = heapq.heappop(max_heap)
            result.append(tweetId)
            tweet_indices[index] -= 1
            if tweet_indices[index] >= 0:
                tweetId, time = self.tweets[users[index]][tweet_indices[index]]
                heapq.heappush(max_heap, (-time, tweetId, index))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


        
