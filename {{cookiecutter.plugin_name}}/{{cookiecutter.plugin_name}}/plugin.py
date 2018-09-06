import formshare.plugins as plugins
import formshare.plugins.utilities as u
from .views import myPublicView,myPrivateView

class {{ cookiecutter.plugin_name }}(plugins.SingletonPlugin):
    plugins.implements(plugins.IRoutes)
    plugins.implements(plugins.IConfig)

    def before_mapping(self, config):
        #We don't add any routes before the host application
        return []

    def after_mapping(self, config):
        #We add here a new route /json that returns a JSON
        custom_map = []
        custom_map.append(u.addRoute('plugin_mypublicview','/mypublicview',myPublicView,'public.jinja2'))
        custom_map.append(u.addRoute('plugin_myprivateview', '/user/{userid}/myprivateview', myPrivateView, 'private.jinja2'))
        return custom_map

    def update_config(self, config):
        #We add here the templates of the plugin to the config
        u.addTemplatesDirectory(config,'templates')

