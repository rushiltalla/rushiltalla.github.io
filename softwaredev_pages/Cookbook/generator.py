import javalang
import os
from jinja2 import Environment, FileSystemLoader
import json
import shutil

GENERATED = "./Recipes/"
DATA = "./data/"


def gen_recipe(file_path):
    base_name = os.path.splitext(os.path.basename(file_path))[0] 

    with open(file_path) as f:
        data = json.load(f)

    # Set up Jinja2 environment and load the template
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('recipe.tmpl')

    # Render the template with data from the JSON file
    output = template.render(
        title=base_name.replace("_", " ").title(),
        ingredients=data['ingredients'],
        steps=data['steps']
    )

    new_filename = GENERATED + base_name + '.html'
    with open(new_filename, 'w') as output_file:
        output_file.write(output)

def gen_main():
    # Generate main file
    print("Gen Main")

def read_recipes(folder_path):
    # List of file names being processed
    # Check each file in folder
    for file in os.listdir(folder_path):
        print(f"- Generating recipe: {file}")
        file_path = os.path.join(folder_path, file)

        gen_recipe(file_path)

    gen_main()


if __name__ == "__main__":
    # Delete the previous generated files
    try:
        shutil.rmtree(GENERATED)
    except FileNotFoundError:
        print("Skipping folder delete!\n")
    
    # Read and generate the recipes
    os.makedirs(os.path.dirname(GENERATED))
    read_recipes(DATA)
