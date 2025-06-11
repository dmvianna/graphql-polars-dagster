import dagster as dg

from example import assets
from example.assets import root_path
from example.dagster_csv import LazyCsvManager

example_assets = dg.load_assets_from_modules([assets])

all_assets_jobs = dg.define_asset_job(name="all_assets_job")

products_job = dg.define_asset_job(name="products_job", selection="products_csv")

defs = dg.Definitions(
    assets=example_assets,
    jobs=[all_assets_jobs, products_job],
    resources={
        "io_manager": LazyCsvManager(root_path=str(root_path)),
    },
)
