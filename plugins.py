"""    <Simple tool to manually find string that need to be translated in a wordpress for cases where you chose to duplicate the site>
    Copyright (C) <2020>  <Shay Gover, ort-israel>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""

from importlib.util import spec_from_file_location, module_from_spec
from settings import settings_dict
from os import chdir

"""
How plugins work?
1) Each plugin has it's own folder under Plugins folder.
2) Each plugin is a packages. 

Plugins names: No commas, colons or equal sign.

To use a plugin: Add it's name to the plugin setting

Plugins should print to output. wpmanualtranslation won't do it for them.
It's recommended to use or at least inherit one of the item classes so it can use it's output printer.
If you inherit you'll have to create a new output function for it.
"""


def load_plugins():
    """
    load all the plugins
    :return: None
    """
    lst_plugins = settings_dict["plugins"].split(",")

    # Changing dir to plugins
    chdir("Plugins")

    for plug in lst_plugins:
        spec = spec_from_file_location(plug, plug)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)

    # Back to the main dir
    chdir("..")

