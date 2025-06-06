import dagster as dg


@dg.asset(io_manager_key="polars_csv_io_manager")
def sales_data():
    return dg.SourceAsset(
        ["sales_data.csv"],
        io_manager_key="polars_csv_io_manager",
    )


@dg.asset(io_manager_key="polars_csv_io_manager")
def sales_reps():
    return dg.SourceAsset(
        ["sales_reps.csv"],
        io_manager_key="polars_csv_io_manager",
    )


@dg.asset(io_manager_key="polars_csv_io_manager")
def products():
    return dg.SourceAsset(
        ["products.csv"],
        io_manager_key="polars_csv_io_manager",
    )
