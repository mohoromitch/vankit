from constants import AppConstant
from pprint import pprint
from clients.instaClient import InstaClient


def run_tw(app, username, password):
    return "Twitter isn't supported yet."


def run_ig(app, username, password):
    try:
        instaClient = InstaClient(username, password)
        return instaClient.generate_report()
    except Exception as e:
        return f"Couldn't log into {app}! {e}"


def run_rd(app, username, password):
    "Reddit isn't supported yet."


dispatch_app = {
    AppConstant.INSTAGRAM: run_ig,
    AppConstant.TWITTER: run_tw,
    AppConstant.REDDIT: run_rd,
}
