import polars as pl
from dagster import ConfigurableIOManager, InputContext, OutputContext
from upath import UPath


class LazyCsvManager(ConfigurableIOManager):
    root_path: str

    def _get_path(self, context: InputContext | OutputContext) -> UPath:
        return UPath(self.root_path).joinpath(UPath(context.asset_key.path))

    def handle_output(self, context: OutputContext, obj: pl.LazyFrame) -> None:
        return obj.sink_csv(self._get_path(context))

    def load_input(self, context: InputContext) -> pl.LazyFrame:
        return pl.scan_csv(self._get_path(context))
