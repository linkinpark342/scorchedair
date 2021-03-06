# This file is part of applesauce.
#
# applesauce is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# applesauce is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with applesace.  If not, see <http://www.gnu.org/licenses/>.
# bootstrap setuptools if necessary

from distribute_setup import use_setuptools
use_setuptools()

VERSION=0.1.1

from setuptools import setup

setup(name="scorchedair",
        version=VERSION,
        packages=["scorchedair"],
        zip_safe=True,
        install_requires = ['pygame'],
        package_data = {
            'applesauce': ['data/sounds/*.ogg'],
        },
)

