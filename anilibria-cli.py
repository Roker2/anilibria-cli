import click
import requests


@click.group()
def cli():
    """..%%%%...%%..%%..%%%%%%..%%......%%%%%%..%%%%%...%%%%%...%%%%%%...%%%%..
.%%..%%..%%%.%%....%%....%%........%%....%%..%%..%%..%%....%%....%%..%%.
.%%%%%%..%%.%%%....%%....%%........%%....%%%%%...%%%%%.....%%....%%%%%%.
.%%..%%..%%..%%....%%....%%........%%....%%..%%..%%..%%....%%....%%..%%.
.%%..%%..%%..%%..%%%%%%..%%%%%%..%%%%%%..%%%%%...%%..%%..%%%%%%..%%..%%.
..................AniLibria-cli от Тортика..............................
........................................................................"""


@click.command()
@click.option('--title', help='Информация об тайтле')
@click.option('--desc', is_flag=True, help='Вывести описание тайтла')
def findtitle(title, desc):
    response = requests.get('https://api.anilibria.tv/v2/searchTitles?search=' + title)
    name = response.json()
    for item in name:
        click.echo(item['names']['ru'] + ' | ' + item['names']['en'])
        if desc:
            click.echo(item['description'])


cli.add_command(findtitle)


@click.command()
@click.option('--desc', is_flag=True, help='Вывести описание тайтла')
def updates(desc):
    response = requests.get('https://api.anilibria.tv/v2/getUpdates')
    data = response.json()
    for item in data:
        click.echo('* '+item['names']['ru'] + ' | ' + item['names']['en'])
        if desc:
            click.echo(item['description'] + '\n')


cli.add_command(updates)


@click.command()
@click.option('--desc', is_flag=True, help='Вывести описание тайтла')
def randomtitle(desc):
    response = requests.get('https://api.anilibria.tv/v2/getRandomTitle')
    name = response.json()
    click.echo(name['names']['ru'] + ' | ' + name['names']['en'])
    if desc:
        click.echo(name['description'])


cli.add_command(randomtitle)


if __name__ == '__main__':
    cli()
