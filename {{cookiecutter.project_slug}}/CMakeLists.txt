cmake_minimum_required(VERSION 3.20)
project({{cookiecutter.project_slug}} C)

include(cmake/CPM.cmake)

CPMAddPackage(
  NAME Format.cmake
  VERSION 1.7.0
  GITHUB_REPOSITORY TheLartians/Format.cmake
  OPTIONS # set to yes skip cmake formatting
          "FORMAT_SKIP_CMAKE NO"
          # path to exclude (optional, supports regular expressions)
          "CMAKE_FORMAT_EXCLUDE cmake/CPM.cmake"
)


add_executable({{cookiecutter.project_slug}} ${PROJECT_SOURCE_DIR}/src/main.c)
target_include_directories({{cookiecutter.project_slug}} PRIVATE ${PROJECT_SOURCE_DIR}/include)
