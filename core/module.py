import importlib
import logging

log = logging.getLogger(__name__)

def load(module_name, config=None):
    try:
        mod = importlib.import_module('modules.{}'.format(module_name))
    except ImportError as error:
        log.fatal('failed to import {}: {}'.format(module_name, str(error)))
        return Error(module_name)
    return getattr(mod, 'Module')(config)

class Module(object):
    def __init__(self, config=None, widgets=[]):
        self._config = config
        self._widgets = widgets if isinstance(widgets, list) else [ widgets ]

    def update(self):
        pass

    def name(self):
        return self.__module__.split('.')[-1]

    def widgets(self):
        return self._widgets

class Error(Module):
    def __init__(self, loaded_module_name):
        self._loaded_module_name = loaded_module_name

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4