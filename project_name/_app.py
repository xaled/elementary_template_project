from os.path import abspath, basename, join

from elementary_flask import ElementaryFlask

module_parent = basename(basename(abspath(__file__)))
template_folder, static_folder = join(module_parent, 'templates'), join(module_parent, 'static')
PROJECT_NAME = 'PROJECT_NAME'
PROJECT_TITLE = 'PROJECT_NAME'

app = ElementaryFlask(PROJECT_NAME,
                      secret='Secretlkjlkdsjhfdsgfd54gf56d456gd4564hgf65h46d4fh',
                      default_title=PROJECT_TITLE,
                      template_folder=template_folder,
                      static_folder=static_folder,
                      theme="adminlte"

                      )
