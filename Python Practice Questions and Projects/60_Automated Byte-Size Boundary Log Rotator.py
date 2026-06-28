import os
from datetime import datetime

LOG_FILE = "system.log"
BACKUP_FILE = "system.log.1"
MAX_SIZE = 5 * 1024  # 5 KB


def append_system_log(message):
    """
    Appends a timestamped message to the system log.
    If the log file exceeds MAX_SIZE, it is rolled over
    to system.log.1 and a new log file is created.
    """

    # Check if rollover is needed
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > MAX_SIZE:

        # Remove existing backup if present
        if os.path.exists(BACKUP_FILE):
            os.remove(BACKUP_FILE)

        # Rename current log to backup
        os.rename(LOG_FILE, BACKUP_FILE)

        print("Rollover executed seamlessly; system.log.1 created.")

    # Create timestamped log entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    # Append entry to the active log
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

    print("Log added.")


# Sample Input
append_system_log("Critical memory warning log flag triggered.")