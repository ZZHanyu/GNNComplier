cmake_minimum_required(VERSION 3.22)
project(CNN_Compiler)

set(CMAKE_CXX_STANDARD 14)

add_executable(CNN_Compiler main.cpp LexAnalysis.h LexAnalysis.cpp)
