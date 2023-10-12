import dearpygui.dearpygui as dpg
from dearpygui_ext import logger

import sys
sys.path.append("d:\\01_Github\\personal\\py_gui_plc\\src")
import py_server
from py_server import connect, disconnect

dpg.create_context()

log=logger.mvLogger()


def button_callback(func):
    status="True"
    def toggle():
        status="True"
        func(status)
        log.log_debug("clicked")
    return toggle

@button_callback
def connect_button(status):
    connect(status)
    log.log_debug("connect")

@button_callback
def disconnect_button(status):
    disconnect(status)
    log.log_debug("disconnect")



with dpg.window(label="Toolbar"):
    # user data set when button is created
    dpg.add_button(label="connect", callback=connect_button, user_data="")

    # user data and callback set any time after button has been created
    dpg.add_button(label="disconnect", tag="btn")
    dpg.set_item_callback("btn", callback=disconnect_button)
    dpg.set_item_user_data("btn", "Some Extra User Data")


dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
