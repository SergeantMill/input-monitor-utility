cmake_minimum_required(VERSION 3.10)
project(input-monitor-utility VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(X11 REQUIRED)

add_executable(input-monitor-utility
    src/main.cpp
    src/keylogger.cpp
    src/file_writer.cpp
)

target_include_directories(input-monitor-utility PRIVATE include)
target_link_libraries(input-monitor-utility PRIVATE X11)

add_executable(test_input_monitor
    tests/test_keylogger.cpp
    src/keylogger.cpp
    src/file_writer.cpp
)

target_include_directories(test_input_monitor PRIVATE include)
target_link_libraries(test_input_monitor PRIVATE X11)