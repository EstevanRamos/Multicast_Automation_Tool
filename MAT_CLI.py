import socket
from rich import print
from rich.prompt import Prompt, IntPrompt
import sys
from os import system
from utils import *


def display_menu(menu):
    """
    Display a menu where the key identifies the name of a function.
    :param menu: dictionary, key identifies a value which is a function name
    :return:
    """
    fun_names = ['List Interfaces',
     'Enable Multicast on Interface',
     'Disable Multicast on Interface',
     'Enables linux to recieve Multicast Traffic',
     'Disables linux to recieve Multicast Traffic',
     'Test Multicast Traffic',
     'Exit',
    ]
    for k, function in menu.items():
        print(k, fun_names[k-1])


def List_Interfaces():
    list_devices()
    Prompt.ask("[bold green]Press Enter to Continue")


def Enable_multicast():
    ops = [i[1] for i in socket.if_nameindex()]
    interface = Prompt.ask("Please Select the Interface to [bold red]ENABLE[/bold red] Multicast", choices=ops)
    enable_mc(interface)
    input("Press Enter to Continue\n")


def Disable_Multicast():
    ops = [i[1] for i in socket.if_nameindex()]
    interface = Prompt.ask("Please Select the Interface to [bold red]DISABLE[/bold red] Multicast", choices=ops)
    disable_mc(interface)
    input("Press Enter to Continue\n")

def Enable_MC_Traffic_linux():
    enable_linux()
    
def Disable_MC_Traffic_linux():
    disable_linux()

def Test_MC_Traffic():
    test_mc_traffic()
    

def done():
    system('clear')  # clears stdout
    print("Goodbye")
    sys.exit()


def main():
    # Create a menu dictionary where the key is an integer number and the
    # value is a function name.
    functions_names = [List_Interfaces, Enable_multicast, Disable_Multicast,Enable_MC_Traffic_linux,Disable_MC_Traffic_linux, Test_MC_Traffic, done]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        selection = IntPrompt.ask("[bold green]Please enter your selection number: ")
        selected_value = menu_items[selection]  # Gets the function name
        selected_value()  # add parentheses to call the function


if __name__ == "__main__":
    main()
