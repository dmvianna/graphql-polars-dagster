from pathlib import Path

import dagster as dg
import polars as pl

fixtures_path = Path(Path(__file__).parent, "..", "tests", "fixtures")


@dg.asset
def sales_csv() -> pl.LazyFrame:
    return pl.scan_csv(fixtures_path / Path("sales_data.csv"))


@dg.asset
def reps_csv() -> pl.LazyFrame:
    return pl.scan_csv(fixtures_path / Path("sales_reps.csv"))


@dg.asset
def products_csv() -> pl.LazyFrame:
    return pl.scan_csv(fixtures_path / Path("products.csv"))


@dg.asset(deps=[sales_csv], io_manager_key="polars_csv_io_manager")
def sales_sink(sales_csv: pl.LazyFrame) -> None:
    return sales_csv.sink_csv(fixtures_path / Path("sales_sink.csv"))
