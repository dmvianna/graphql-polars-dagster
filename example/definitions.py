from pathlib import Path

import dagster as dg

from example import assets
from example.dagster_csv import PolarsCsvIOManager

example_assets = dg.load_assets_from_modules([assets])

fixtures_path = str(Path(Path(__file__).parent, "..", "tests", "fixtures"))

defs = dg.Definitions(
    assets=example_assets,
    resources={"polars_csv_io_manager": PolarsCsvIOManager(base_dir=fixtures_path)},
)
