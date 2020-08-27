import click
from pprint import pprint
from instaClient import InstaClient

from constants import INSTAGRAM, TWITTER
from constants import APP_INPUT_MAP

def start_twitter(app, username, password):
    click.echo("Twitter isn't supported yet.")

def start_instagram(app, username, password):
    click.echo("Attempting logging in as %s..." % username)
    instaClient = InstaClient(username, password)
    pprint(instaClient.getFollowersUsernames())
    pprint(instaClient.getFollowingUsernames())
    pprint(instaClient.getFollowersNotFollowingBack())
    pprint(instaClient.getFollowingNotFollowingBack())

app_router = {
    INSTAGRAM: start_instagram, 
    TWITTER: start_twitter
}

def validate_app(ctx, param, value):
    if value not in APP_INPUT_MAP:
        click.echo("{} is not a supported application.".format(value))
        click.echo(APP_INPUT_MAP)
        ctx.exit()
    return value

def validate_username(ctx, param, value):
    if " " in value:
        click.echo("Your username cannot contain spaces.")
        ctx.exit()
    return value

@click.command()
@click.option("--app", prompt="Which app to log into", help="The webapp you want to use.", callback=validate_app)
@click.option("--username", prompt="Please enter your username", help="Your app specific login username", callback=validate_username)
@click.option("--password", prompt="Please enter your password", help="Your app specific login password", hide_input=True)
def start(app, username, password):
    click.echo("Logging into {} for {}".format(APP_INPUT_MAP[app], username))
    app_router[APP_INPUT_MAP[app]](app, username, password)

if __name__ == "__main__": 
    start(None, None, None)