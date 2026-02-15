

def compute_consistency_rank(df, columns_scored):
    rank_columns = [col for col in df.columns if col.endswith(f"-{columns_scored}")]

    if not rank_columns:
        raise ValueError(f"A consistency ranking column of name:{columns_scored}, is required")

    average_name = f"{columns_scored}-average-rank"
    df[average_name] = df[rank_columns].mean(axis=1)

    df[f"{columns_scored}-rank-consistency"] = df[average_name].rank(ascending=True, method="dense")
    return df
