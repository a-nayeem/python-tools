import sys
import argparse
import os.path
from datetime import datetime
from rich.console import Console
from dns import resolver,reversename

console = Console()
## Setting up argparser

parser = argparse.ArgumentParser(description='This program performs reverse dns lookup')
parser.add_argument('-i', required=True)             #setting the argument '-file' as required. without '-file' argument the program will not run.
args = parser.parse_args()
ip = args.i


def main():
    try:
        ns = str(resolver.resolve(reversename.from_address(ip), 'PTR')[0])
        console.print(ns, style="bold green")
    except resolver.NXDOMAIN:
        console.print("The DNS Query Name does not exist", style="bold red") 
        
        

    
if __name__ == "__main__":
    main()