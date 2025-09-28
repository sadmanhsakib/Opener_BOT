# Cache-RemoverBOT
This is a single Python script that opens websites and desktop applications. Upon opening, the script also writes (creates, if the log file does not exist) the number of times the script ran(both today and lifetime). Also, logs the time and date for each time the script ran.
<h3>How does it work?</h3>
The user has to add the URLs and shortcuts as mentioned later. The script at first looks for a "log.txt" in its local directory. If there is no "log.txt" file, then it automatically creates one. After that, it opens the websites and applications as per the user's wish. After opening the applications and websites successfully, it logs the time in the log.txt file. 

<h3>How to use?</h3>
0. Download the dotenv library using "pip install dotenv" in PowerShell or CMD. <br> 
1. Download the GitHub repository.<br>
2. Unzip the repository.<br>
3. Create a ".env" file in the same directory and open it. <br>
4. Write: URLS="". Add the paths inside the double inverted commas. Be sure to separate the paths with a comma(,) in between and ensure that there are no whitespaces. <br>
5. On the next line in the ".env" folder, write: SHORTCUTS="". Add the paths that you want to delete every week in here.<br>
6. Open the Task Scheduler.<br>
7. Create a new task for the script. (Trigger can be whatever the user wants. Personally, I set my trigger when the user logs on. Then the script runs again and again every 3 hours indefinitely .)<br>
