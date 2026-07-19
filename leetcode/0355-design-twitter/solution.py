from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]: # merge k sorted lists
        heap = []
        users = self.followees[userId] | {userId}

        for user in users:
            for time, tweet in self.tweets[user]:
                heapq.heappush(heap, (-time, tweet))

        ans = []

        while heap and len(ans) < 10:
            ans.append(heapq.heappop(heap)[1])

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
