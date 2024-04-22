
# SMTP Server Checker

This Python script checks the validity of SMTP servers listed in a text file. It attempts to establish a connection to each server using the provided credentials and logs the results to a file.

## Features

- Multi-threaded SMTP server checking for efficiency.
- Logging of successful and failed attempts.
- Colorized console output for easy reading.
- Supports both IPv4 and IPv6 addresses.

## Requirements

- Python 3.x
- colorama library (install via `pip install colorama`)

## Usage

1. Clone or download the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Prepare a text file containing SMTP server details in the format `server|port|username|password`, with each entry on a new line.
4. Run the script by executing `python smtp_checker.py`.
5. Follow the on-screen prompts to provide the path to your SMTP server list file.
6. Sit back and wait for the script to complete. The results will be logged to a file named `Work-Smtps.txt`.

## Example SMTP List File

```bash
smtp.example.com|587|user@example.com|password123
mail.server.com|25|admin@mail.com|securePass
```

## Output

- Successful connections will be logged in `result-Smtps.txt` in the format `server|port|username|password`.
- Failed connections will be logged in the console and the log file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


