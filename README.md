# Marketfeed-Assignment-Implementation PDF: [Click here! ](https://drive.google.com/file/d/1B4wfbcm9mCM754RYHRBNFOajsUwgdOKj/view?usp=sharing) 
This repository hosts two Python scripts for log management tasks. The first script offers real-time monitoring of log files with the ability to gracefully stop the monitoring loop. It serves as a valuable tool for troubleshooting and system maintenance. The second script enhances functionality by providing real-time monitoring and basic log analysis, including keyword counting and summary report generation. These scripts provide essential tools for efficient log management and troubleshooting tasks.

Please refer to the provided Implementation PDF for detailed insights into how the scripts are implemented 


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

### 1. Logging Configuration (`logging.basicConfig()`)
   - Configures the root logger to output log messages with a level of DEBUG or higher.

### 2. Logger Initialization
   - Creates a logger named `__name__`, typically corresponding to the module's name.

### 3. Log Message Formats
   - Defines message formats for different log levels (`INFO`, `DEBUG`, `ERROR`).

### 4. Log Levels
   - Contains logging levels (`INFO`, `DEBUG`, `ERROR`) to cycle through for logging messages.

### 5. Monitoring Log File
   - Monitors a log file for errors.
   - Utilizes PowerShell to continuously read the log file with `subprocess.Popen`.
   - Performs basic log analysis by counting occurrences of lines containing "ERROR" using `Counter`.
   - Generates a summary report based on error counts.

### 6. Main Loop
   - Controls the program flow.
   - Sets up log file path and initiates an infinite loop.
   - Randomly selects a log level and logs a message using the chosen level.
   - Retrieves log entries and summary reports from `monitor_log_file()` and prints them.
   - Handles exceptions like `StopIteration` and `KeyboardInterrupt` to exit gracefully.

### 7. Analysis
   - Provides a real-time analysis of log entries.
   - Summarizes error occurrences to offer insights into the log's health and potential issues.


