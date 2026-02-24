"""Main file for generating results for sample lines-pay game."""

from gamestate import GameState
from game_config import GameConfig
from game_optimization import OptimizationSetup
from optimization_program.run_script import OptimizationExecution
from utils.game_analytics.run_analysis import create_stat_sheet
from utils.rgs_verification import execute_all_tests
from src.state.run_sims import create_books
from src.write_data.write_configs import generate_configs

if __name__ == "__main__":

    num_threads = 10
    rust_threads = 20
    batching_size = 5000
    compression = True
    profiling = False

    num_sim_args = {
        "base": int(1e5),  # 100,000 spins - BLOCKER FIX
    }

    run_conditions = {
        "run_sims": True,
        "run_optimization": False,
        "run_analysis": False,
        "run_format_checks": False,
    }
    target_modes = list(num_sim_args.keys())

    config = GameConfig()
    gamestate = GameState(config)

    if run_conditions["run_sims"]:
        create_books(
            gamestate,
            config,
            num_sim_args,
            batching_size,
            num_threads,
            compression,
            profiling,
        )

    generate_configs(gamestate)
    print("✅ Books generation complete")
