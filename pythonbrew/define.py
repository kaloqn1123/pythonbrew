import os

VERSION = "0.6"

if os.environ.has_key("PYTHONBREW_ROOT"):
    ROOT = os.environ["PYTHONBREW_ROOT"]
else:
    ROOT = os.path.join(os.environ["HOME"],".pythonbrew")

INSTALLER_ROOT = os.path.dirname(os.path.abspath(__file__))

PATH_PYTHONS = os.path.join(ROOT,"pythons")
PATH_BUILD = os.path.join(ROOT,"build")
PATH_DISTS = os.path.join(ROOT,"dists")
PATH_ETC = os.path.join(ROOT,"etc")
PATH_BIN = os.path.join(ROOT,"bin")
PATH_LOG = os.path.join(ROOT,"log")
PATH_SCRIPTS = os.path.join(ROOT,"scripts")
PATH_SCRIPTS_PYTHONBREW = os.path.join(PATH_SCRIPTS,"pythonbrew")
PATH_SCRIPTS_PYTHONBREW_COMMANDS = os.path.join(PATH_SCRIPTS_PYTHONBREW,"commands")
PATH_PATCHES = os.path.join(ROOT,"patches")
PATH_PATCHES_MACOSX = os.path.join(PATH_PATCHES,"macosx")
PATH_PATCHES_MACOSX_PYTHON25 = os.path.join(PATH_PATCHES_MACOSX,"python25")
PATH_PATCHES_MACOSX_PYTHON24 = os.path.join(PATH_PATCHES_MACOSX,"python24")

# file path
PATH_BIN_PYTHONBREW = os.path.join(PATH_BIN,"pythonbrew")
PATH_BIN_PYBREW = os.path.join(PATH_BIN,"pybrew") # pybrew is symlink as pythonbrew

# download setuptools url 
DISTRIBUTE_SETUP_DLSITE = "http://python-distribute.org/distribute_setup.py"

# download pythonbrew url
PYTHONBREW_UPDATE_URL = {
    "head": "http://github.com/utahta/pythonbrew/tarball/master",
    "0.5": "https://github.com/utahta/pythonbrew/tarball/0.5",
    "0.6": "https://github.com/utahta/pythonbrew/tarball/0.6",
}

# download Python package url
PYTHON_PACKAGE_URL = {}
PYTHON_PACKAGE_URL["1.5.2"] = "http://www.python.org/ftp/python/src/py152.tgz"
PYTHON_PACKAGE_URL["1.6.1"] = "http://www.python.org/download/releases/1.6.1/Python-1.6.1.tar.gz"
_PYTHON_PACKAGE_VERSIONS = [
    "2.0", "2.0.1",
    "2.1", "2.1.1", "2.1.2", "2.1.3",
    "2.2", "2.2.1", "2.2.2", "2.2.3",
    "2.3", "2.3.1", "2.3.2", "2.3.4", "2.3.5", "2.3.6", "2.3.7",
    "2.4", "2.4.1", "2.4.2", "2.4.3", "2.4.4", "2.4.5", "2.4.6",
    "2.5", "2.5.1", "2.5.2", "2.5.3", "2.5.4", "2.5.5",
    "2.6", "2.6.1", "2.6.2", "2.6.3", "2.6.4", "2.6.5", "2.6.6",
    "2.7",
    "3.0", "3.0.1",
    "3.1", "3.1.1", "3.1.2",
]
for version in _PYTHON_PACKAGE_VERSIONS:
    PYTHON_PACKAGE_URL[version] = "http://www.python.org/ftp/python/%s/Python-%s.tgz" % (version, version)
del _PYTHON_PACKAGE_VERSIONS
PYTHON_PACKAGE_URL["3.2a1"] = "http://www.python.org/ftp/python/3.2/Python-3.2a1.tgz"
PYTHON_PACKAGE_URL["3.2a2"] = "http://www.python.org/ftp/python/3.2/Python-3.2a2.tgz"
PYTHON_PACKAGE_URL["3.2a3"] = "http://www.python.org/ftp/python/3.2/Python-3.2a3.tgz"

LATEST_VERSIONS_OF_PYTHON = ['1.5.2', '1.6.1', 
                             '2.0.1', '2.1.3', '2.2.3', '2.3.7', '2.4.6', '2.5.5', '2.6.6', '2.7', 
                             '3.0.1', '3.1.2', '3.2a3']


