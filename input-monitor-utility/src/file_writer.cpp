#include "file_writer.h"
#include <iostream>

FileWriter::FileWriter(const std::string& filename) {
    file.open(filename, std::ios::app);
    if (!file.is_open()) {
        std::cerr << "Failed to open file: " << filename << "\n";
    }
}

FileWriter::~FileWriter() {
    if (file.is_open()) {
        file.close();
    }
}

void FileWriter::write(const std::string& data) {
    if (file.is_open()) {
        file << data;
        file.flush();
    }
}

void FileWriter::flush() {
    if (file.is_open()) {
        file.flush();
    }
}