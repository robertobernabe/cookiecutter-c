import os


VCPKG_GITHUB_REPO = "{{cookiecutter.vcpkg_github_repo}}"
VCPKG_TAG = "{{cookiecutter.vcpkg_tag}}"

os.system("git init")
# os.system("git remote add")
os.system("git submodule add https://github.com/{} vcpkg".format(VCPKG_GITHUB_REPO))
os.chdir("vcpkg")
os.system("git checkout {0} && echo {0}".format(VCPKG_TAG))
os.system("bootstrap-vcpkg")
os.chdir("..")
