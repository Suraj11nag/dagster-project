from dagster import Definitions, load_assets_from_modules

from .assets import mongodb
from dagster_embedded_elt.dlt import DagsterDltResource

mongodb_assets = load_assets_from_modules([mongodb])
# main entry point in dagster
defs = Definitions(
    assets=[*mongodb_assets],
    resources={
        "dlt": DagsterDltResource()
    }
)
