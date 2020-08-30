from pprint import pformat
from InstagramAPI import InstagramAPI
from clients.baseclient import BaseClient, formatted_section

FOLLOWERS_SECTION_TITLE = "Your followers:\n"
FOLLOWING_SECTION_TITLE = "You're following:\n"
FOLLOWERS_NOT_FOLLOWING_BACK = ("Who's following you "
                                "that you're not following back:\n")
FOLLOWING_NOT_FOLLOWING_BACK = ("Who you're following "
                                "that is not following back:\n")


class InstaClient(BaseClient):
    def __init__(self, username, password):
        """Initialize the client
        Note, this attempts to log into the underlying client API
        and will raise an error if unsuccessful"""
        self.username = username,
        self.client = InstagramAPI(username, password)
        self.followers = []
        self.following = []

        self.client.login()

    def generate_report(self) -> str:
        rs = []
        rs.append(self.__report_followers_section())
        rs.append(self.__report_following_section())
        rs.append(self.__report_followers_not_following_back())
        rs.append(self.__report_following_not_following_back())

        return ''.join(rs)

    @formatted_section
    def __report_followers_section(self) -> str:
        return FOLLOWERS_SECTION_TITLE + pformat(
            self.get_followers_usernames())

    @formatted_section
    def __report_following_section(self) -> str:
        return FOLLOWING_SECTION_TITLE + pformat(
            self.get_following_usernames())

    @formatted_section
    def __report_followers_not_following_back(self) -> str:
        return FOLLOWERS_NOT_FOLLOWING_BACK + pformat(
            self.get_followers_not_following_back())

    @formatted_section
    def __report_following_not_following_back(self) -> str:
        return FOLLOWING_NOT_FOLLOWING_BACK + pformat(
            self.get_following_not_following_back())

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
