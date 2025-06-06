from typing import TYPE_CHECKING, Any, Optional, cast

import polars as pl
from dagster._core.execution.context.input import InputContext
from dagster._core.execution.context.output import OutputContext
from dagster_polars import BasePolarsUPathIOManager
from pyarrow.fs import LocalFileSystem

if TYPE_CHECKING:
    from upath import UPath


class PolarsCsvIOManager(BasePolarsUPathIOManager):
    """
    Implements reading and writing Polars DataFrames in CSV format.
    """

    def write_df_to_path(self, context: OutputContext, df: pl.DataFrame, path: "UPath"):
        context_metadata = context.definition_metadata or {}
        fs = path.fs if hasattr(path, "fs") else None
        if fs is not None:
            with fs.open(str(path), mode="wb") as f:
                df.write_csv(
                    f,  # type: ignore
                    **context_metadata,
                )

    def sink_df_to_path(self, context: OutputContext, df: pl.LazyFrame, path: "UPath"):
        context_metadata = context.definition_metadata or {}

        fs = path.fs if hasattr(path, "fs") else None
        if isinstance(fs, LocalFileSystem):
            df.sink_csv(str(path), **context_metadata)
        else:
            context.log.warning(
                "Cloud sink is not possible yet, instead it's dispatched to pyarrow writer which collects it into memory first.",
            )
            return self.write_df_to_path(context, df.collect(), path)

    def scan_df_from_path(self, path: "UPath", context: InputContext) -> pl.LazyFrame:
        context_metadata = context.definition_metadata or {}

        return pl.scan_csv(path, **context_metadata)
