import logging
import time
import random
import subprocess
from collections import Counter

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
        error_counter = Counter()
        for line in iter(tail_process.stdout.readline, b''):
            log_entry = line.decode().strip()
            # Perform basic log analysis
            if "ERROR" in log_entry:
                error_counter[log_entry] += 1
            # Generate summary report
            summary_report = ""
            if len(error_counter) > 0:
                summary_report += "\nError Summary:\n"
                for error, count in error_counter.most_common():
                    summary_report += f"{error}: {count} occurrences\n"
            yield log_entry, summary_report
    except KeyboardInterrupt:
        print("\nMonitoring interrupted. Exiting.")
    finally:
        tail_process.terminate()

# Main loop to log messages and monitor log file
def main():
    log_file_path = "log_file.log"  # Replace with the actual path to your log file
    log_generator = monitor_log_file(log_file_path)
    while True:
        try:
            # Randomly select a log level
            log_level = random.choice(log_levels)
            # Get the log message format for the selected log level
            log_message = formats[log_level]
            # Log the message
            logger.log(log_level, log_message)
            # Get log entry and summary report
            log_entry, summary_report = next(log_generator)
            # Print log entry
            print(log_entry)
            # Print summary report
            if summary_report:
                print(summary_report)
            # Sleep for a short interval
            time.sleep(1)
        except StopIteration:
            print("\nEnd of log file reached. Exiting.")
            break
        except KeyboardInterrupt:
            print("\nLogging interrupted. Exiting.")
            break


if __name__ == "__main__":
    main()
