from pathlib import Path

import dagster as dg
import polars as pl
from upath import UPath

default_root_path = Path(Path(__file__).parent, "..", "tests", "fixtures").__str__()
root_path: UPath = UPath(dg.EnvVar("ROOT_PATH").get_value(default_root_path))


@dg.asset
def reps_csv() -> pl.LazyFrame:
    return pl.scan_csv(root_path / Path("sales_reps.csv"))


@dg.asset
def sales_csv() -> pl.LazyFrame:
    return pl.scan_csv(root_path / Path("sales_data.csv"))


@dg.asset
def products_csv() -> pl.LazyFrame:
    return pl.scan_csv(root_path / Path("products.csv"))


@dg.asset
def sales_sink(sales_csv: pl.LazyFrame) -> None:
    """
    Notice that because we are using an IO manager, we do not need to
    define the dependency in the decorator. We just use its name in an
    argument and we are good to go!
    """
    return sales_csv.sink_csv(root_path / Path("sales_sink.csv"))
