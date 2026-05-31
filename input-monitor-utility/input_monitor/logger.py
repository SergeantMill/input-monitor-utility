"""Logging module for key events."""
import os
from datetime import datetime

class KeyLogger:
    """Handles writing key events to a log file."""
    
    def __init__(self, filename="keylog.txt"):
        self.filename = filename
        self._ensure_file()
    
    def _ensure_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write(f"Input Monitor Log - {datetime.now()}\n")
                f.write("=" * 50 + "\n")
    
    def log_key(self, key_char, timestamp=None):
        """Write a key press to the log file."""
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, 'a') as f:
            f.write(f"[{timestamp}] {key_char}\n")
    
    def log_special(self, key_name, timestamp=None):
        """Write a special key press (e.g., ENTER, SHIFT) to the log."""
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, 'a') as f:
            f.write(f"[{timestamp}] <{key_name}>\n")