import click
from auth import Auth
from pprint import pprint
from dispatch import dispatch_app

from constants import AppConstant
from constants import APP_INPUT_MAP


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
@click.option("--app",
              prompt="Which app to log into",
              help="The webapp you want to use.",
              callback=validate_app)
@click.option("--username",
              prompt="Please enter your username",
              help="Your app specific login username",
              callback=validate_username)
def prompt_main(app, username):
    auth = Auth(app)
    password = auth.getPassword(username)

    if not password:
        print(f"No saved password found for {username}...")
        password = click.prompt("Please enter your password",
                                type=str,
                                hide_input=True)
    else:
        print(f"{app} password found for {username}!")

    should_save_password = str(click.prompt("Remember this password "
                                            "in Keychain? [y/n]",
                                            type=str)).strip().lower() == "y"

    if should_save_password:
        print("Saving password in keychain...")
        auth.setPassword(username, password)

    print("Logging into {} for {}".format(APP_INPUT_MAP[app], username))
    dispatch_app[APP_INPUT_MAP[app]](app, username, password)


if __name__ == "__main__":
    prompt_main(None, None)
