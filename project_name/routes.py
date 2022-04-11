from ._app import elementary


@elementary.route_page('/', page_layout='default', navigation=True, navigation_title='Home',
                       navigation_icon='fas fa-home')
def cheat_sheet():
    return 'Hello World'
