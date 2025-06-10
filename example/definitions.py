import dagster as dg

from example import assets
from example.assets import fixtures_path
from example.dagster_csv import LazyCsvManager

example_assets = dg.load_assets_from_modules([assets])


defs = dg.Definitions(
    assets=example_assets,
    resources={
        "lazy_csv_manager": LazyCsvManager(root_path=str(fixtures_path)),
    },
)
