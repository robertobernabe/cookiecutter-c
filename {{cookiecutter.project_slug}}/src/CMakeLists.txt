add_executable({{cookiecutter.project_slug}} main.c)
target_include_directories({{cookiecutter.project_slug}} PRIVATE ${PROJECT_SOURCE_DIR}/include)
