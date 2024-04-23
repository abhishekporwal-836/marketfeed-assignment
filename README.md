# Marketfeed-Assignment

## Description

# Implementation PDF: [Click here! ](https://drive.google.com/file/d/1B4wfbcm9mCM754RYHRBNFOajsUwgdOKj/view?usp=sharing)

## TASKS:


# Log Monitoring Script

## Description
This script continuously logs messages at random levels (INFO, DEBUG, ERROR) and monitors the log file concurrently.



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
