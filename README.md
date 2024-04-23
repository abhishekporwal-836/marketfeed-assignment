# Marketfeed-Assignment Implementation PDF: [Click here! ](https://drive.google.com/file/d/1B4wfbcm9mCM754RYHRBNFOajsUwgdOKj/view?usp=sharing)

This repository hosts two Python scripts for log management tasks. The first script offers real-time monitoring of log files with the ability to gracefully stop the monitoring loop. It serves as a valuable tool for troubleshooting and system maintenance. The second script enhances functionality by providing real-time monitoring and basic log analysis, including keyword counting and summary report generation. These scripts provide essential tools for efficient log management and troubleshooting tasks.

Please refer to the provided Implementation PDF for detailed insights into how the scripts are implemented.

To access the scripts directly, you can find them here:
- [Log Monitoring Script](log_monitor.py)
- [Log Monitoring and Analysis Script](log_analysis.py)

## TASKS:
1. [Log File Monitoring](#1-Log-File-Monitoring)
2. [Log Analysis](#2-Log-analysis)

# 1) Log File Monitoring: 

### 1. Imported Modules
   The script imports the following necessary modules:
   - logging
   - time
   - random
   - subprocess

### 2. Logging Configuration (`logging.basicConfig()`)
   Configures the root logger to output log messages with a level of DEBUG or higher.

### 3. Logger Initialization
   Creates a logger named `__name__`, typically corresponding to the module's name.

### 4. Log Message Formats
   Defines a dictionary `formats` that maps logging levels (INFO, DEBUG, ERROR) to corresponding message formats.

### 5. Log Levels and Selection
   Defines a list `log_levels` containing logging levels to cycle through (INFO, DEBUG, ERROR).
   Randomly selects a log level from this list.

### 6. Logging Loop (`while True`)
   Enters an infinite loop to repeatedly log messages and monitor the log file.
   Inside the loop:
   - Randomly selects a log level.
   - Retrieves the message format for the selected log level.
   - Logs a message with the selected log level using `logger.log()`.
   - Monitors the log file using `monitor_log_file()` function.
   - Sleeps for a short interval (1 second).

### 7. Monitoring Log File (`monitor_log_file()`)
   This function monitors the specified log file continuously.
   It uses a subprocess to run a PowerShell command (`Get-Content -Wait`) to continuously read the log file.
   It prints each line from the log file to the console.
   It terminates when a keyboard interrupt (Ctrl+C) is detected.

### 8. Keyboard Interrupt Handling
   The script handles keyboard interrupts (`KeyboardInterrupt`) gracefully, printing appropriate messages and breaking out of the main loop.



# 2) Log Analysis:

### 1. Description
- The script continuously monitors a specified log file for new entries in real-time.
- It uses PowerShell's Get-Content cmdlet with the -Wait parameter to achieve real-time monitoring on Windows systems.
- Log entries are read line by line from the log file as they are appended.

### 2. Log Analysis
- The script performs basic analysis on the log entries, focusing on error messages.
- It counts occurrences of error messages in the log file using a Counter object from the collections module.
- The error summary report includes the count of each unique error message encountered in the log file.

### 3. Script Execution
- The main loop of the script simulates logging messages at random INFO, DEBUG, or ERROR log levels.
- It logs messages using the Python logging module.
- The script integrates the log monitoring and analysis functionalities within this loop.
- While logging messages, it simultaneously monitors the log file for new entries and performs analysis on those entries.
- The script continues execution until interrupted by the user (e.g., with Ctrl+C).

### 4. Functioning
- Upon running the script, it begins logging messages and monitoring the specified log file.
- As new log entries are added to the file, they are read and displayed in the console in real-time.
- When an error message is encountered, the script counts its occurrences and displays a summary report of error messages along with the log entry.
- The script continues to log messages and monitor the log file until it's interrupted or reaches the end of the file.
- Users can interrupt the script at any time using Ctrl+C in the terminal/command prompt.

