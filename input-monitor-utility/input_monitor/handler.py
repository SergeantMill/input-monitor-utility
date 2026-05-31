"""Keyboard event handler using pynput."""
from pynput import keyboard
from .logger import KeyLogger

class KeyHandler:
    """Listens for and processes keyboard events."""
    
    def __init__(self, logger=None):
        self.logger = logger or KeyLogger()
        self.listener = None
        self.running = False
    
    def on_press(self, key):
        """Callback for key press events."""
        try:
            if hasattr(key, 'char') and key.char is not None:
                self.logger.log_key(key.char)
            else:
                key_name = str(key).replace('Key.', '').upper()
                self.logger.log_special(key_name)
                if key == keyboard.Key.esc:
                    return False  # Stop listener
        except Exception as e:
            print(f"Error logging key: {e}")
        return True
    
    def start(self):
        """Start the keyboard listener."""
        if self.running:
            print("Already running.")
            return
        self.running = True
        print("Input Monitor started. Press ESC to stop.")
        with keyboard.Listener(on_press=self.on_press) as self.listener:
            self.listener.join()
        self.running = False
        print("Input Monitor stopped.")
    
    def stop(self):
        """Stop the keyboard listener."""
        if self.listener and self.listener.running:
            self.listener.stop()
        self.running = False