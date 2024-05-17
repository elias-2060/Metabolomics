cmake_minimum_required(VERSION 3.10)
project(untitled1)

set(CMAKE_CXX_STANDARD 17)


add_executable(join_R_A join_R_A.cpp
        Table.cpp
        Table.h)

add_executable(untitled2
        joinRA_D.cpp Table.cpp
        Table.h)
