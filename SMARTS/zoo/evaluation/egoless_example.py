import argparse

import gymnasium as gym

from smarts.core.utils.episodes import episodes

if __name__ == "__main__":
    parser = argparse.ArgumentParser("hiway-egoless-example")
    parser.add_argument("replay_data", help="Replay data path", type=str)

    parser.add_argument(
        "scenarios",
        help="A list of scenarios. Each element can be either the scenario to run "
        "(see scenarios/ for some samples you can use) OR a directory of scenarios "
        "to sample from.",
        type=str,
        nargs="+",
    )
    parser.add_argument(
        "--headless", help="run simulation in headless mode", action="store_true"
    )
    args = parser.parse_args()

    data_replay_path = (
        f"./{args.replay_data}/{args.scenarios[0].split('/')[-1]}/data_replay"
    )
    env = gym.make(
        "smarts.env:hiway-v1",
        scenarios=args.scenarios,
        agent_interfaces={},
        headless=args.headless,
        fixed_timestep_sec=0.1,
        envision_record_data_replay_path=data_replay_path,
    )

    for episode in episodes(n=1):
        env.reset()
        episode.record_scenario(env.scenario_log)

        for _ in range(600):
            env.step({})
            episode.record_step({}, {}, {}, {}, {})

    env.close()
