from functions.compute_consistency_rank import compute_consistency_rank
from functions.compute_ranking import compute_ranking
from utils.read_files import read_json, read_csv
from functions.compute_weighted_score import compute_weighted_score
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def current_flow():
    standard_csv_config_file = "configs/generic_file_structure.json"
    standard_csv_config = read_json("configs/generic_file_structure.json")
    config = None
    df = None
    file_name = None # Can be set by argparse

    config = config if config else standard_csv_config_file
    config = read_json(config)
    file_name = file_name if file_name else config["file_name"]

    if not (config["column_headers_row"] == standard_csv_config["column_headers_row"] and
        config["column_headers_column_start"] == standard_csv_config["column_headers_column_start"] and
        config["data_column_start"] == standard_csv_config["data_column_start"] and
        config["data_column_end"] == standard_csv_config["data_column_end"] and
        config["data_row_start"] == standard_csv_config["data_row_start"] and
        config["data_row_end"] == standard_csv_config["data_row_end"]
    ):
        # TODO: Perform DF manipulation to meet actual format -> finalDF
        print("hello")
    else:
        df = read_csv(file_name)

    for profile_name, profile_weights in config["profiles"].items():
        df[f"{profile_name}-weighted"] = compute_weighted_score(df,config["metrics"], profile_weights)

    df = compute_ranking(df, columns_scored="weighted")

    df = compute_consistency_rank(df, "weighted-rank")

    df.to_csv("output.csv", index=False)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    current_flow()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Required Args:
# config_file
# file_name