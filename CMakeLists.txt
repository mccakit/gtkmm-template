set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
cmake_minimum_required(VERSION 3.20)
project(GTKTest LANGUAGES C CXX)
find_package(PkgConfig REQUIRED)
pkg_check_modules(GTKMM REQUIRED IMPORTED_TARGET gtkmm-4.0)
add_executable(main main.cpp)
target_include_directories(main PRIVATE ${GTKMM_INCLUDE_DIRS})
target_link_libraries(main PRIVATE ${GTKMM_LIBRARIES})
target_link_directories(main PRIVATE ${GTKMM_LIBRARY_DIRS})
set(CMAKE_BUILD_TYPE RELEASE)
set_target_properties(main PROPERTIES
    BUILD_RPATH "$ORIGIN/../lib"
    INSTALL_RPATH "$ORIGIN/../lib"
)
