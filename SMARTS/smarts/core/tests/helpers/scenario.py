# MIT License
#
# Copyright (C) 2021. Huawei Technologies Co., Ltd. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import shutil
import tempfile
from contextlib import contextmanager
from pathlib import Path

from smarts.sstudio.sumo2mesh import generate_glb_from_sumo_file


@contextmanager
def temp_scenario(name: str, map: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        scenario = Path(temp_dir) / name
        scenario.mkdir()

        test_maps_dir = Path(__file__).parent.parent
        shutil.copyfile(test_maps_dir / map, scenario / "map.net.xml")
        generate_glb_from_sumo_file(str(scenario / "map.net.xml"), str(scenario))

        yield scenario


def maps_dir():
    """Add a maps directory."""
    return Path(__file__).parent.parent / "maps"
