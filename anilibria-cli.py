import click
import requests


@click.group()
def cli():
    """Anilibria-cli от Тортика"""


@click.command()
@click.option('--title', help='Информация об тайтле')
def find(title):
    response = requests.get('https://api.anilibria.tv/v2/searchTitles?search='+title)
    name = response.json()
    for item in name:
        click.echo(item['names']['ru'])


cli.add_command(find)


if __name__ == '__main__':
    cli()
