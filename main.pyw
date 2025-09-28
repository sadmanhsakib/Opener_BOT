import webbrowser
import os
import datetime
from dotenv import load_dotenv

load_dotenv(".env")

counter = 0
today_counter = 0

# creating a new log file if there is no log file
if not (os.path.exists("log.txt")):
    # creates a new log file
    with open("log.txt", 'w') as file:
        # writing the initial lines
        file.write(f"Number of times Opened Lifetime = {counter}\n")
        file.write(f"Number of times Opened Today = {today_counter}\n")
        
log_file = "log.txt"

def main():
    with open(log_file, 'r') as file:
        # getting the counter values
        lines = file.readlines()
        counter = lines[0].replace("Number of times Opened Lifetime = ", "")
        today_counter = lines[1].replace("Number of times Opened Today = ", "")

    # adjusting the counter values
    counter = int(counter)
    counter += 1
    today_counter = int(today_counter)
    today_counter += 1
    
    open_sites()
    log_event(counter, today_counter)

def open_sites():
    # for opening the websites
    urls = os.getenv("URLS")
    for url in urls.split(','):
        webbrowser.open(url)

    # for opening the applications through their shortcuts
    apps = os.getenv("SHORTCUTS")
    for app in apps.split(','):
        os.startfile(app)

def log_event(counter, today_counter):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # reseting the today counter if it's a new day
    today_counter = is_new_day(today_counter)

    # logging the current run time in log file
    with open(log_file, 'a') as file:
        file.write(f"{today_counter}. {now}\n")

    # opening the log file in read mode and storing the lines in a list
    with open(log_file, 'r') as old_file:
        lines = old_file.readlines()
    os.remove(log_file)

    # updating the initial lines with recent value
    lines[0] = lines[0].replace(f"{lines[0]}", f"Number of times Opened Lifetime = {counter}\n")
    lines[1] = lines[1].replace(f"{lines[1]}", f"Number of times Opened Today = {today_counter}\n")

    # creating a new log file and writing down the lines
    with open(log_file, 'w') as new_file:
        new_file.writelines(lines)

def is_new_day(today_counter):
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    
    with open(log_file, 'r') as file:
        lines = file.readlines()
        # getting the last line of the log file
        last_line = lines[-1]
    # creates a list of words that was in that string
    parts = last_line.split()

    # index 1 word is the date, comparing it with today's date
    if today != parts[1]:
        # opening the file to add a new line
        with open(log_file, 'a') as file:
            file.write("[New Day]\n")
        # resetting the today_counter back to zero
        today_counter = 1
    return today_counter


main()