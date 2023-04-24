import io

from interfaces.command_line_interface import CommandLineInterface
from system import PublishingSystem

if __name__=='__main__':
    interface = CommandLineInterface(publishing_system=PublishingSystem(), output_stream=io.open('/dev/stdin'))

    while True:
        interface.process_input()
