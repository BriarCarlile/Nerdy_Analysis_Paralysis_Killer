
def compute_ranking(df, ascending=False, method="min", columns_scored="weighted"):
    score_columns = [col for col in df.columns if col.endswith(f"-{columns_scored}")]

    for score_column in score_columns:
        profile_name = score_column.replace(columns_scored, "")
        rank_col = f"{profile_name}{columns_scored}-rank"
        df[rank_col] = df[score_column].rank(ascending=ascending, method=method)

    return df