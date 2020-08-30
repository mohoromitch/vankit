from InstagramAPI import InstagramAPI
from clients.client import Client


class InstaClient:
    def __init__(self, username, password):
        """Initialize the client
        Note, this attempts to log into the underlying client API
        and will raise an error if unsuccessful"""
        self.username = username,
        self.client = InstagramAPI(username, password)
        self.followers = []
        self.following = []

        self.client.login()

    def get_followers_usernames(self):
        """return the account's followers, lazy loaded"""
        if not self.followers:
            for item in self.client.getTotalSelfFollowers():
                self.followers.append(item.get('username'))
        return self.followers

    def get_following_usernames(self):
        """return the accounts followed by this account, lazy loaded"""
        if not self.following:
            for item in self.client.getTotalSelfFollowings():
                self.following.append(item.get('username'))
        return self.following

    def get_followers_not_following_back(self):
        return [f for f in self.get_followers_usernames()
                if f not in self.get_following_usernames()]

    def get_following_not_following_back(self):
        return [f for f in self.get_following_usernames()
                if f not in self.get_followers_usernames()]
