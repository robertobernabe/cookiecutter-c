project({{cookiecutter.project_slug}} C)
add_executable({{cookiecutter.project_slug}} ${PROJECT_SOURCE_DIR}/src/main.c)
target_include_directories({{cookiecutter.project_slug}} PRIVATE ${PROJECT_SOURCE_DIR}/include)
