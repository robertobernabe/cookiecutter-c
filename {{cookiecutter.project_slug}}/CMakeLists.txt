cmake_minimum_required(VERSION 3.14)

if(NOT DEFINED VCPKG_ROOT)
  set(VCPKG_ROOT
      ${CMAKE_CURRENT_SOURCE_DIR}/vcpkg
      CACHE PATH "Path to vcpkg directory")
endif()

set(VCPKG_APPINSTALL_DEPS ON)
set(VCPKG_APPLOCAL_DEPS_INSTALL ON)
set(X_VCPKG_APPLOCAL_DEPS_INSTALL ON)

if(DEFINED VCPKG_ROOT)
  set(CMAKE_TOOLCHAIN_FILE
      "${VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
      CACHE PATH "Path to vcpkg toolchain")
  if(NOT EXISTS "${CMAKE_TOOLCHAIN_FILE}")
    message(
      FATAL_ERROR
        "Invalid CMAKE_TOOLCHAIN_FILE specified (${CMAKE_TOOLCHAIN_FILE}, ${VCPKG_ROOT}); please specify an absolute path"
    )
  endif()
endif()

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

add_subdirectory(src)
include(CTest)
# add_subdirectory(test)
