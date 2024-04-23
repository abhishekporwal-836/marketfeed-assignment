import logging
import time
import random
import subprocess

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the root logger level to DEBUG

# Create a logger
logger = logging.getLogger(__name__)

# Define log message formats
formats = {
    logging.INFO: "INFO message",
    logging.DEBUG: "DEBUG message",
    logging.ERROR: "ERROR message"
}

# Define log levels to cycle through
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]

def monitor_log_file(log_file_path):
    try:
        tail_process = subprocess.Popen(['powershell', '-Command', f'Get-Content -Wait -Path "{log_file_path}"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        for line in iter(tail_process.stdout.readline, b''):
            print(line.decode().strip())
    except KeyboardInterrupt:
        print("\nMonitoring interrupted. Exiting.")
    finally:
        tail_process.terminate()

# Main loop to log messages
while True:
    try:
        # Randomly select a log level
        log_level = random.choice(log_levels)
        # Get the log message format for the selected log level
        log_message = formats[log_level]
        # Log the message
        logger.log(log_level, log_message)
        # Monitor log file
        log_file_path = "log_file.log"  # Replace with the actual path to your log file
        monitor_log_file(log_file_path)
        # Sleep for a short interval
        time.sleep(1)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nLogging interrupted. Exiting.")
        break
