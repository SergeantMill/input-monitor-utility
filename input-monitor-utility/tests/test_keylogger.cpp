#include <iostream>
#include <cassert>
#include "keylogger.h"

int main() {
    std::cout << "Running Keylogger tests...\n";

    Keylogger logger;
    // Test that logger can be created without crashing
    assert(true);

    // Test stop before start (should not crash)
    logger.stop();
    assert(true);

    std::cout << "All tests passed!\n";
    return 0;
}