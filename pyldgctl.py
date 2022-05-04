#!/usr/bin/env python3	
#
# File: pyldgctl.py
#
# Copyright (c) 2022 Ben Kuhn
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  
# 02110-1301, USA.
#


# Import GObject and require GTK 3.0
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk

# Import Socket for endianness conversion functions
import socket

# Import configparser for the configuration file
import configparser

# Import pyserial
import serial

# GUI stuffs
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="PyLDGCtl")
        self.set_border_width(10)
        self.set_default_size(800, 400)

        # Header Bar
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "LDG Tuner Control"
        self.set_titlebar(hb)

        # Draw Settings Button
        settingsButton = Gtk.Button()
        settingsIcon = Gio.ThemedIcon(name="system-settings-symbolic")
        settingsImage = Gtk.Image.new_from_gicon(settingsIcon, Gtk.IconSize.BUTTON)
        settingsButton.add(settingsImage)
        hb.pack_end(settingsButton)

        #Create Labels for the Meters
        self.swrMeterLabel = Gtk.Label(label="SWR")
        self.powerMeterLabel = Gtk.Label(label="Power")

        # Set up the Meters
        self.powerMeter = Gtk.LevelBar.new_for_interval(0,1000)
        self.swrMeter = Gtk.LevelBar.new_for_interval(1,3)

        # Create the Meter Reading Labels
        powerMeterValue = 0
        swrMeterValue = 1
        self.powerValueLabel = Gtk.Label(str(powerMeterValue) + "W")
        self.swrValueLabel = Gtk.Label(str(swrMeterValue) + ":1")

        # Set up the Buttons
        

        # Set up widget Layout
        grid = Gtk.Grid(column_homogeneous=True, column_spacing=2, row_spacing=2)
        grid.add(self.powerMeterLabel)
        grid.attach(self.powerMeter, 1, 0, 4, 1)
        grid.attach(self.powerValueLabel, 5, 0, 1, 1)
        grid.attach(self.swrMeterLabel, 0, 1, 1, 1)
        grid.attach(self.swrMeter, 1, 1, 4, 1)
        grid.attach(self.swrValueLabel, 5, 1, 1, 1)


        # Add the grid containing all the widgets
        self.add(grid)

        # Adjust the CSS to make the meters thicker
        css = b'''
        levelbar, trough { 
            min-height: 15px;
        }
        '''
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(css)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


# Function to decode the power readings from the meter
def decodePwr(raw)

    # 0 to 100 Watts
    if raw < 256:
        result = (float(raw) / 255) * 100

    # 100 to 1000 Watts
    else:
        raw -= 256
        result = 100 * (900 * (float(raw)/768))
    return result



