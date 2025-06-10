import dagster as dg

from example import assets
from example.assets import fixtures_path
from example.dagster_csv import PolarsCsvIOManager

example_assets = dg.load_assets_from_modules([assets])

defs = dg.Definitions(
    assets=example_assets,
    resources={
        "polars_csv_io_manager": PolarsCsvIOManager(base_dir=str(fixtures_path))
    },
)
