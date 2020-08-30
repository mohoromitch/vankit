from constants import AppConstant
from pprint import pprint
from clients.instaClient import InstaClient


def run_tw(app, username, password):
    print("Twitter isn't supported yet.")


def run_ig(app, username, password):
    try:
        print("Attempting logging in as %s..." % username)
        instaClient = InstaClient(username, password)
        print("Your followers:")
        pprint(instaClient.get_followers_usernames())
        print("You're following:")
        pprint(instaClient.get_following_usernames())
        print("Who's following you that you're not following back:")
        pprint(instaClient.get_followers_not_following_back())
        print("Who you're following that is not following back:")
        pprint(instaClient.get_following_not_following_back())
    except Exception:
        return (f"Couldn't log into {app}!")


def run_rd(app, username, password):
    print("Reddit isn't supported yet.")


dispatch_app = {
    AppConstant.INSTAGRAM: run_ig,
    AppConstant.TWITTER: run_tw,
    AppConstant.REDDIT: run_rd,
}
