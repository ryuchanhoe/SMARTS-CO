# Copyright (C) 2022. Huawei Technologies Co., Ltd. All rights reserved.
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

import random
from itertools import combinations
from pathlib import Path

from smarts.sstudio import gen_scenario
from smarts.sstudio.types import (
    Distribution,
    Trip,
    Mission,
    Route,
    Scenario,
    Traffic,
    TrafficActor,
    TrapEntryTactic,
)

vehicle1 = TrafficActor(
    name="vehicle1",
    accel = 0,
    decel = 0,
    emergency_decel = 0,
    depart_speed = random.uniform(5, 8),
    max_speed = 15
)

# vehicle2 = TrafficActor(

# )

traffic = {}

traffic['vehicle1'] = Traffic(
    engine = "SUMO",
    flows = [],
    trips = [
        Trip(
            vehicle_name = "vehicle1",
            route = Route(
                    begin=("E0", 0, random.uniform(30, 50)),
                    end=("E0", 0, "max"),
                ),
        )
    ]
)



gen_scenario(
    scenario=Scenario(
        traffic=traffic,
        # ego_missions=ego_missions,
    ),
    output_dir=Path(__file__).parent,
)
