cmake_minimum_required(VERSION 3.10)
project(uuid_to_shellcode)

set(CMAKE_CXX_STANDARD 11)

# Add the src directory
add_executable(uuid_to_shellcode
    src/load.cpp
    src/payload.h
)

target_include_directories(uuid_to_shellcode PRIVATE src)