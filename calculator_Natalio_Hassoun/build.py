"""Build, test, check, and package the Lab 6 calculator."""

from pybuilder.core import Author, init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.distutils")

name = "calculator_Natalio_Hassoun"
version = "0.1.0"
summary = "Lab 6 calculator with automated PyBuilder and Make builds"
authors = [
    Author("Natalio Hassoun", "235908789+NatalioH@users.noreply.github.com")
]
url = "https://github.com/NatalioH/Lab6_Natalio_Hassoun"
requires_python = ">=3.10"
default_task = ["analyze", "publish"]


@init
def initialize(project):
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property(
        "dir_source_unittest_python", "tests/unittest/calculator_Natalio_Hassoun"
    )
    project.set_property("unittest_module_glob", "test_*")
    project.set_property("flake8_max_line_length", 88)
    project.set_property("flake8_break_build", True)
    project.set_property("distutils_commands", ["sdist", "bdist_wheel"])
    project.build_depends_on("flake8", "==7.3.0")
