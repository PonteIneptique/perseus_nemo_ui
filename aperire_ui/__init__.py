# -*- coding: utf-8 -*-

from flask_nemo.plugin import PluginPrototype
from pkg_resources import resource_filename


class AperireUI(PluginPrototype):
    """
        The Breadcrumb plugin is enabled by default in Nemo.
        It can be overwritten or removed. It simply adds a breadcrumb

    """
    HAS_AUGMENT_RENDER = False
    TEMPLATES = {
        "main": resource_filename("aperire_ui", "data/templates/main"),
        "arethusa": resource_filename("aperire_ui", "data/templates/arethusa")
    }
    CSS = [resource_filename("aperire_ui","data/assets/css/theme-ext.css")]

