cmake_minimum_required(VERSION 3.10)

# Project name
project(DailyCodingProblems)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Google Test
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

# Find all .cpp files in the current directory
file(GLOB CPP_FILES "problems/*.cpp")

# Create executables for each .cpp file
foreach(cpp_file ${CPP_FILES})
    # Get filename without extension
    get_filename_component(exe_name ${cpp_file} NAME_WE)
    
    # Create executable
    add_executable(${exe_name} ${cpp_file})
    
    # Link Google Test libraries
    target_link_libraries(${exe_name} ${GTEST_LIBRARIES} pthread)
    
    # Optional: Set output directory
    set_target_properties(${exe_name} PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    )
endforeach()

# Alternative: If you want to compile a specific file, uncomment and modify:
# add_executable(problem334 334-problem-2025-08-04.cpp)