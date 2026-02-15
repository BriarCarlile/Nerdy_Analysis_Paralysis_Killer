from content.functions.compute_consistency_rank import compute_consistency_rank
from content.functions.compute_ranking import compute_ranking
from content.utils.create_radar_chart import create_multiple_radar_chart
from content.utils.read_files import read_json, read_csv
from content.functions.compute_weighted_score import compute_weighted_score
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def current_flow():
    standard_csv_config_file = "../../content/configs/generic_file_structure.json"
    standard_csv_config = read_json("content/configs/generic_file_structure.json")
    config = "scope_file_structure.json"
    df = None
    file_name = "../../scope_data.csv"  # Can be set by argparse

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

    columns = [col for col in df.columns if col.endswith("-weighted") ]

    create_multiple_radar_chart(df, columns, "Weighted Score by Use Case")


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