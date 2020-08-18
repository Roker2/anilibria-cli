import click
import requests
import os


def get_ru_en_name(item):
    return item['names']['ru'] + ' | ' + item['names']['en']


def show_titles_list(url, desc):
    # Generate separator line, if desc is True
    if desc:
        # Get rows and columns of terminal
        # Rows is unneeded value
        _, columns = os.popen('stty size', 'r').read().split()
        # Generate separator line
        separator_line = ''
        for i in range(int(columns)):
            separator_line += '━'
    response = requests.get(url)
    data = response.json()
    for item in data:
        click.echo('* ' + get_ru_en_name(item))
        if desc:
            click.echo(item['description'])
            click.echo(separator_line)
    return response


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
    show_titles_list('https://api.anilibria.tv/v2/searchTitles?search=' + title, desc)


cli.add_command(findtitle)


@click.command()
@click.option('--desc', is_flag=True, help='Вывести описание тайтла')
def updates(desc):
    show_titles_list('https://api.anilibria.tv/v2/getUpdates', desc)


cli.add_command(updates)


@click.command()
@click.option('--desc', is_flag=True, help='Вывести описание тайтла')
def randomtitle(desc):
    response = requests.get('https://api.anilibria.tv/v2/getRandomTitle')
    name = response.json()
    click.echo(get_ru_en_name(name))
    if desc:
        click.echo(name['description'])


cli.add_command(randomtitle)


if __name__ == '__main__':
    cli()
