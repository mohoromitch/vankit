import click
from pprint import pprint
from auth import Auth
from instaClient import InstaClient

from constants import AppConstant
from constants import APP_INPUT_MAP

def run_tw(app, username, password):
    click.echo("Twitter isn't supported yet.")

def run_ig(app, username, password):
    try:
        print("Attempting logging in as %s..." % username)
        instaClient = InstaClient(username, password)
        print("Your followers:")
        pprint(instaClient.getFollowersUsernames())
        print("You're following:")
        pprint(instaClient.getFollowingUsernames())
        print("Who's following you that you're not following back:")
        pprint(instaClient.getFollowersNotFollowingBack())
        print("Who you're following that is not following back:")
        pprint(instaClient.getFollowingNotFollowingBack())
    except Exception:
        print(f"Couldn't log into {app}!")
        return

app_router = {
    AppConstant.INSTAGRAM: run_ig, 
    AppConstant.TWITTER: run_tw
}

def validate_app(ctx, param, value):
    if value not in APP_INPUT_MAP:
        click.echo("{} is not a supported application.".format(value))
        click.echo(APP_INPUT_MAP)
        ctx.exit()
    return APP_INPUT_MAP.get(value)

def validate_username(ctx, param, value):
    if " " in value:
        click.echo("Your username cannot contain spaces.")
        ctx.exit()
    return value

@click.command()
@click.option("--app", prompt="Which app to log into", help="The webapp you want to use.", callback=validate_app)
@click.option("--username", prompt="Please enter your username", help="Your app specific login username", callback=validate_username)
def prompt_main(app, username):

    password = Auth.getPassword(app, username)

    if not password:
        print(f"No saved password found for {username}...")
        password = click.prompt("Please enter your password", type=str, hide_input=True)
    else:
        print(f"{app} password found for {username}!")

    should_save_password = str(click.prompt("Do you want to save this password in Keychain? [y/n]", type=str)).strip().lower() == "y"

    if should_save_password:
        print("Saving password in keychain...")
        Auth.setPassword(app, username, password)

    print("Logging into {} for {}".format(APP_INPUT_MAP[app], username))
    app_router[APP_INPUT_MAP[app]](app, username, password)

if __name__ == "__main__": 
    prompt_main(None, None)