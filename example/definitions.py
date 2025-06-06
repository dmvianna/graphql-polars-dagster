from pathlib import Path

import dagster as dg

from example import assets
from example.assets import products, sales_data, sales_reps
from example.dagster_csv import PolarsCsvIOManager

assets = dg.load_assets_from_modules([assets])

fixtures_path = str(Path(Path(__file__).parent, "..", "tests", "fixtures"))

defs = dg.Definitions(
    assets=[sales_data, products, sales_reps],
    resources={"polars_csv_io_manager": PolarsCsvIOManager(base_dir=fixtures_path)},
)
