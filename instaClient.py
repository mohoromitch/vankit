from InstagramAPI import InstagramAPI

class InstaClient:
    def __init__(self, username, password):
        self.username = username,
        self.client = InstagramAPI(username, password) 
        self.followers = []
        self.following = []

        self.client.login()

    def getFollowersUsernames(self):
        """return the account's followers, lazy loaded"""
        if not self.followers:
            for item in self.client.getTotalSelfFollowers():
                self.followers.append(item.get('username'))
        return self.followers

    def getFollowingUsernames(self):
        """return the accounts followed by this account, lazy loaded"""
        if not self.following:
            for item in self.client.getTotalSelfFollowings():
                self.following.append(item.get('username'))
        return self.following
    
    def getFollowersNotFollowingBack(self):
        return [f for f in self.getFollowersUsernames() if f not in self.getFollowingUsernames()]

    def getFollowingNotFollowingBack(self): 
        return [f for f in self.getFollowingUsernames() if f not in self.getFollowersUsernames()]