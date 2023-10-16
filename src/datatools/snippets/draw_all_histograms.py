import math
from functools import partial
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


def draw_all_histograms(
    df: pd.DataFrame,
    per_row: int = 4,
    figsize: tuple[int, int] = (20, 8),
    hist_kwargs: dict[str, Any] = {},
) -> None:
    fig = plt.figure(figsize=figsize)  # noqa: F841

    hist_kwargs = {"bins": 50, "color": "blue", "alpha": 1} | hist_kwargs

    n_cols = len(df.columns)
    n_row = math.ceil(n_cols / per_row)

    set_subplot = partial(plt.subplot, n_row, per_row)

    for i, column in enumerate(df.columns, 1):
        set_subplot(i)
        plt.hist(df[column], **hist_kwargs)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()
