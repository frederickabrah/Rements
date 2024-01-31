# DoS Attack Tool

This is a simple Denial of Service (DoS) attack tool written in Python.
The tool allows you to send a specified number of requests to a target URL using multiple threads.
Please note that DoS attacks are illegal unless you have proper authorization to test or evaluate the security of a system. Misuse of this tool can lead to serious legal consequences. Use it responsibly and only with permission from the target system's owner.
Also has A GUI interface with a pinger to check your success
## Usage
1. Make sure you have Python 3 installed.
2. Install the required dependencies using the `pip install -r requirements.txt` command.
3. Execute the tool using the `./rements or python3 rements` command.
4. Follow the prompts or provide command-line arguments to specify the target URL, number of threads, and number of requests per thread.
5. Optionally, enable verbose output using the `-v` flag.
6. The tool will start sending requests and display information about each request.
7. Once the desired number of requests have been sent, the tool will display "DoS attack finished!".

## Command-line Arguments
- `-u/--url`: Specify the target URL.
- `-w/--threads`: Specify the number of threads.
- `-r/--requests`: Specify the number of requests per thread.
- `-v/--verbose`: Enable verbose output.

## Creator
This tool was created by Frederick Abraham.
- Facebook Account: [Frederick Abraham](https://www.facebook.com/profile.php?id=100091418762784)
