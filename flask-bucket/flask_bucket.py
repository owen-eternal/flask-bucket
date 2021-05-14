import os
import click

class FlaskBusket():
    def __init__(self, app):
        self.app = app
        if self.app is not None:
            self.init_app(app)

    def init_app(self, app):
        @app.cli.command('make_module')
        @click.argument('module_name')
        def make_module(module_name):

            #create directory
            module_path = os.path.join(self.app.root_path, module_name)
            os.makedirs(module_path + '/templates')

            #call the make file function and pass the module path and name as args
            self.__make_files(module_path, module_name)
        
        app.cli.add_command(make_module)
        
    def __make_files(self, mod_path, mod_name):
        #create files inside the directory
        files = ['__init__.py', 'routes.py']
        #iterate through each file and create a file path 
        for each_file in files: 
            file = os.path.join(mod_path, each_file)
            #write file
            with open(file, 'w') as f:
                #write code inside the routes.py files
                if f.name.endswith('routes.py'):
                    f.write('from flask import Blueprint \n\n')
                    f.write(f'"""All your {mod_name} routes are located here. NB: register Blueprint inside flask app factory""" \n\n')
                    f.write(f'{mod_name} = Blueprint("{mod_name}", __name__, template_folder="templates")\n\n')
                    f.write(f'@{mod_name}.route("/blueprint")\ndef helloworld():\n\t return "Hello World"')