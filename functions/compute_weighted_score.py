
import pandas as pd

from functions.target_equations import lower_target, higher_target

def compute_weighted_score(df, metrics, profile_weights):
    score = pd.Series(0.0, index=df.index)
    total_weight = sum(profile_weights.values())

    for metric, weight in profile_weights.items():
        if metric not in df.columns:
            continue

        target = metrics[metric]['direction']
        col_data = df[metric]

        min_val = col_data.min()
        max_val = col_data.max()

        if min_val == max_val:
            normalized = pd.Series(0.5, index=df.index)
        elif target == "lower":
            normalized = lower_target(col_data, max_val, min_val)
        elif target == "higher":
            normalized = higher_target(col_data, max_val, min_val)
        else:
            raise ValueError("Unknown target '{}'".format(target))

        score += normalized.fillna(0) * weight/total_weight

    return score



