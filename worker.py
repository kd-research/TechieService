import agentops
import sys
import os
import base64
from os import path
from subprocess import run, DEVNULL
from tempfile import TemporaryDirectory

def llm_work(description):
    # Modify this function only
    from techies import cli as techies_cli

    agentops.init(auto_start_session=False)

    agentops.start_session()
    hierarchy_crew = techies_cli.get_openai_crew('hierarchy_crew_v2')
    hierarchy_crew.kickoff(inputs={'game_specifications': description})

    del hierarchy_crew

    files = set(os.listdir()) - {'game_hierarchy.xml', 'agentops.log'}
    for file in files:
        os.remove(file)

    agentops.start_session()
    html5_crew = techies_cli.get_openai_crew('html5_crew')
    html5_crew.kickoff(inputs={'game_specifications': description})

    del html5_crew

def embed_audio_base64_in_html(html_file_path, sound_folder):
    # Read the HTML content
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Supported audio file extensions
    audio_extensions = ['.mp3', '.wav']

    # Loop through all files in the sound folder
    for filename in os.listdir(sound_folder):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in audio_extensions:
            audio_file_path = os.path.join(sound_folder, filename)
            with open(audio_file_path, 'rb') as audio_file:
                # Convert the audio file to Base64
                base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')

            # Determine the MIME type based on the file extension
            mime_type = f'audio/{file_ext[1:]}'

            # Replace occurrences of the audio file path in the HTML content
            # This will handle both <audio> tags and any JavaScript code
            html_content = html_content.replace(filename, f"data:{mime_type};base64,{base64_audio}")

    # Write the modified HTML content back to a new file or overwrite the original file
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

def clean_html(file_path, output_path=None):
    # Load the content of the HTML file
    with open(file_path, "r") as file:
        html_content = file.read()

    # Find the starting point of the HTML content
    start_index = html_content.find("<!DOCTYPE html>")
    # Find the ending point of the HTML content
    end_index = html_content.find("</html>") + len("</html>")

    # Extract the content between <!DOCTYPE html> and </html>
    cleaned_html_content = html_content[start_index:end_index]

    # If output_path is provided, save the cleaned content to a new file
    if output_path:
        with open(output_path, "w") as cleaned_file:
            cleaned_file.write(cleaned_html_content)
        print(f"Cleaned HTML content saved to {output_path}")

    return cleaned_html_content

# Deprecated
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
    embed_audio_base64_in_html('game.html', '.')
    clean_html('game.html', 'game.html')
    sys.exit(0)
