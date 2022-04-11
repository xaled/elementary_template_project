from os.path import abspath, dirname, join

from flask import Flask

from elementary_flask import ElementaryFlask

module_dir = dirname(abspath(__file__))
template_folder, static_folder = join(module_dir, 'templates'), join(module_dir, 'static')
PROJECT_NAME = 'PROJECT_NAME'
PROJECT_TITLE = 'PROJECT_NAME'

app = Flask(PROJECT_NAME, template_folder=template_folder, static_folder=static_folder, root_path=dirname(module_dir))
elementary = ElementaryFlask(PROJECT_NAME, app,
                             default_title=PROJECT_TITLE,
                             theme="adminlte"
                             )
