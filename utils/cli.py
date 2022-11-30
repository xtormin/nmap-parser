import sys
import argparse

parser = argparse.ArgumentParser(add_help = True, description = '%(prog)s hunts all forms and inputs found in a list of urls.')

parser.add_argument('-x','--nmapxmlfile', 
                    help = 'XML output of nmap scan', 
                    nargs = '?', type=str)
parser.add_argument('-C','--csvfile', 
                    help = 'Output to CSV',
                    action= "store_true")
parser.add_argument('-X','--xsltfile', 
                    help = 'Output to XLSX',
                    action= "store_true") 
parser.add_argument('-v','--verbose', 
                    help = 'Verbose', action= "store_true")

def get():
    return parser.parse_args()

def help():
    return parser.print_help(sys.stderr)