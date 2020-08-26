import click
from pprint import pprint
from instaAPI import InstaAPI

instagram = "instagram" 
twitter = "twitter"

app_mapping = {
    "instagram": instagram,
    "i": instagram,
    "twitter": twitter,
    "t": twitter
} 

def start_twitter(app, username, password):
    click.echo("Twitter isn't supposed yet.")

def start_instagram(app, username, password):
    click.echo("Attempting logging in as %s..." % username)
    instaAPI = InstaAPI(username, password)
    pprint(instaAPI.getFollowersUsernames())
    pprint(instaAPI.getFollowingUsernames())
    pprint(instaAPI.getFollowersNotFollowingBack())
    pprint(instaAPI.getFollowingNotFollowingBack())

app_router = {
    instagram: start_instagram, 
    twitter: start_twitter
}

def validate_app(ctx, param, value):
    if value not in app_mapping:
        click.echo("{} is not a supported application.".format(value))
        click.echo(app_mapping)
        ctx.exit()
    return value

def validate_username(ctx, param, value):
    if " " in value:
        click.echo("Your username cannot contain spaces.")
        ctx.exit()
    return value

@click.command()
@click.option("--app", prompt="Which app to log into:", help="The webapp you want to use.", callback=validate_app)
@click.option("--username", prompt="Please enter your username:", help="Your app specific login username", callback=validate_username)
@click.option("--password", prompt="Please enter your password:", help="Your app specific login password", hide_input=True)
def start(app, username, password):
    click.echo("Logging into {} for {}".format(app_mapping[app], username))
    app_router[app_mapping[app]](app, username, password)

if __name__ == "__main__": 
    start()