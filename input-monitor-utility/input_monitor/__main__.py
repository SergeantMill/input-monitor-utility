"""Entry point for running as a module: python -m input_monitor"""
from .handler import KeyHandler

def main():
    handler = KeyHandler()
    try:
        handler.start()
    except KeyboardInterrupt:
        handler.stop()
        print("\nInterrupted by user.")

if __name__ == "__main__":
    main()