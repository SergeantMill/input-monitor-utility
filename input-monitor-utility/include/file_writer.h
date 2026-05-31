#ifndef FILE_WRITER_H
#define FILE_WRITER_H

#include <string>
#include <fstream>

class FileWriter {
public:
    FileWriter(const std::string& filename);
    ~FileWriter();
    void write(const std::string& data);
    void flush();

private:
    std::ofstream file;
};

#endif