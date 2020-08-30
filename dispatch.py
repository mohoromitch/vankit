from constants import AppConstant
from pprint import pprint
from clients.instaClient import InstaClient


def run_tw(app, username, password):
    print("Twitter isn't supported yet.")


def run_ig(app, username, password):
    try:
        print("Attempting logging in as %s..." % username)
        instaClient = InstaClient(username, password)
        print(instaClient.generate_report())
    except Exception:
        return (f"Couldn't log into {app}!")


def run_rd(app, username, password):
    print("Reddit isn't supported yet.")


dispatch_app = {
    AppConstant.INSTAGRAM: run_ig,
    AppConstant.TWITTER: run_tw,
    AppConstant.REDDIT: run_rd,
}
