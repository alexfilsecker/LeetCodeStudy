"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/design-twitter/description/
Basic Description:
    Create a simple version of tweeter
"""

from typing import List, Union, Tuple, Dict, Set


class Twitter:

    def __init__(self):
        self.tweets: List[Tuple[int, int]] = []
        self.followees: Dict[int, Set[int]] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ensureSelfFollow(userId)
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        count = 0
        feed: List[int] = []
        for posterId, tweetId in reversed(self.tweets):
            if count >= 10:
                break
            if userId in self.followees[posterId]:
                feed.append(tweetId)
                count += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.ensureSelfFollow(followeeId)
        self.followees[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.ensureSelfFollow(followeeId)
        if followerId in self.followees[followeeId]:
            self.followees[followeeId].remove(followerId)

    def ensureSelfFollow(self, userId: int) -> None:
        if userId not in self.followees:
            self.followees[userId] = {userId}


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


def run(methods: List[str], args: List[List[str]]) -> List[Union[bool, None]]:
    action_dict = {
        "Twitter": Twitter.__init__,
        "postTweet": Twitter.postTweet,
        "getNewsFeed": Twitter.getNewsFeed,
        "follow": Twitter.follow,
        "unfollow": Twitter.unfollow,
    }
    obj = Twitter()
    result = [None]
    for i in range(1, len(methods)):
        method = methods[i]
        arg = args[i]
        result.append(action_dict[method](obj, *arg))

    return result


if __name__ == "__main__":
    methods = [
        "Twitter",
        "postTweet",
        "getNewsFeed",
        "follow",
        "postTweet",
        "getNewsFeed",
        "unfollow",
        "getNewsFeed",
    ]
    args = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    print(run(methods, args))
