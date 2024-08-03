import sys
import os
from os import path
from subprocess import run, DEVNULL
from tempfile import TemporaryDirectory

def llm_work(description):
    # Modify this function only
    from techies import cli as techies_cli

    hierarchy_crew = techies_cli.get_openai_crew('hierarchy_crew_v2')
    hierarchy_crew.kickoff(inputs={'game_specifications': description})
    del hierarchy_crew

    files = set(os.listdir()) - {'game_hierarchy.xml'}
    for file in files:
        os.remove(file)

    html5_crew = techies_cli.get_openai_crew('html5_crew')
    html5_crew.kickoff()
    del html5_crew

    with open('game.html', 'rb') as f:
        data = f.read()

    return data

def generate_game_html(description):
    cwd = os.getcwd()
    try:
        with TemporaryDirectory() as temp_dir:
            os.chdir(temp_dir)
            data = llm_work(description)
    finally:
        os.chdir(cwd)

    return data

if __name__ == '__main__':
    description = sys.argv[1]
    llm_work(description)
    sys.exit(0)
