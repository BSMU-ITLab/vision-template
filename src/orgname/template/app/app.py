from bsmu.vision.app import App

from orgname.template import __title__, __version__


class TemplateApp(App):
    TITLE = __title__
    VERSION = __version__
