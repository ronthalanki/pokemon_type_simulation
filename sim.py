import json
import random
import logging
import tqdm
import matplotlib.pyplot as plt

from helper import single_type_battle, dual_type_battle, Type, BattleResult


def sim(number_of_battles_per_round: int, number_of_rounds: int, types_file_name: str, dual_type: bool = False, plotFigure: bool = False):
    logger = logging.getLogger('sim')

    types_data, type_simulation_results = load_json_type_data(types_file_name, dual_type)
    plot_weights = []

    for round_number in tqdm.tqdm(range(number_of_rounds)):
        current_type_weights = [type_simulation_results[type]
                                ['weights'] for type in type_simulation_results]
        plot_weights.append(current_type_weights)

        logger.info(
            f'Current type weights: {__current_weights_to_string(type_simulation_results, current_type_weights)}')

        for _ in range(number_of_battles_per_round):
            # Weighted random select two types
            type1, type2 = random.choices(
                list(type_simulation_results.keys()), weights=current_type_weights, k=2)

            if not dual_type:
                result = single_type_battle(types_data, type1, type2)
            else:
                result = dual_type_battle(types_data, type1, type2)

            if result == BattleResult.WIN:
                type_simulation_results[type1]['wins'] += 1
                type_simulation_results[type2]['losses'] += 1
                logger.debug(f'{type1} is stronger than {type2}')

            elif result == BattleResult.DRAW:
                # Randomly pick a winner
                if random.choice([True, False]):
                    type_simulation_results[type1]['wins'] += 1
                    type_simulation_results[type2]['losses'] += 1
                    logger.debug(
                        f'{type1} draws {type2}, randomly selected {type1}')
                else:
                    type_simulation_results[type2]['wins'] += 1
                    type_simulation_results[type1]['losses'] += 1
                    logger.debug(
                        f'{type1} draws {type2}, randomly selected {type2}')

            elif result == BattleResult.LOSE:
                type_simulation_results[type2]['wins'] += 1
                type_simulation_results[type1]['losses'] += 1
                logger.debug(f'{type2} is stronger than {type1}')

        # Print results ordered by win percentage and clear the wins and losses
        for type_name in sorted(type_simulation_results, key=lambda x: 1.0 * type_simulation_results[x]['wins'] / (type_simulation_results[x]['wins'] + type_simulation_results[x]['losses']), reverse=True):
            number_of_battles = type_simulation_results[type_name]['wins'] + \
                type_simulation_results[type_name]['losses']
            win_percentage = 1.0 * \
                type_simulation_results[type_name]['wins'] / number_of_battles

            type_simulation_results[type_name]['weights'] = win_percentage

            logger.info(
                f'Round number {round_number} - {type_name}: {win_percentage:.3f} win percentage, {number_of_battles} number of battles')

    current_type_weights = [type_simulation_results[type]
                            ['weights'] for type in type_simulation_results]
    plot_weights.append(current_type_weights)

    # print results of weights after all rounds, sorted by weight
    for type_name in sorted(type_simulation_results, key=lambda x: type_simulation_results[x]['weights'], reverse=True):
        logger.warning(f'{type_name}: {type_simulation_results[type_name]["weights"]}')

    if plotFigure:
        plt.figure()
        plt.plot(plot_weights)

        # add legend
        plt.legend(list(type_simulation_results.keys()))
        plt.show()

    return type_simulation_results


def load_json_type_data(types_file_name: str, dual_type: bool = False):
    types_data = {}
    type_simulation_results = {}

    with open(types_file_name) as json_file:
        json_types_data = json.load(json_file)
        for type in json_types_data:
            types_data[type['name']] = Type(type)

            type_simulation_results[type['name']] = {
                'weights': 0.5,
                'wins': 0,
                'losses': 0,
            }

    if dual_type:
        for type1 in list(types_data.keys()):
            for type2 in list(types_data.keys()):
                if type1 != type2:
                    type_simulation_results[f'{type1},{type2}'] = {
                        'weights': 0.5,
                        'wins': 0,
                        'losses': 0,
                    }
    return types_data, type_simulation_results


def __current_weights_to_string(type_simulation_results: dict, current_type_weights: list) -> str:
    return "".join(f"{type}: {current_type_weights[i]:3f} " for i, type in enumerate(type_simulation_results))
