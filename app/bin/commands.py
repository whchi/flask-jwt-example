
import click
from flask import Blueprint
import uuid
from ..database.models import AppAccount

passport = Blueprint('passport', __name__)

@passport.cli.command('create')
@click.argument('account')
def create_appaccount(account):
    password = uuid.uuid4().hex
    try:
        app = AppAccount(account=account,password=password)
        app.hash_password()
        app.save()
        click.echo('===============================')
        click.echo('new account created')
        click.echo('account: ' + account)
        click.echo('passowrd: ' + password)
    except Exception as e:
        click.echo(str(e))
