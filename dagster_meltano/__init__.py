from dagster import resource

from dagster_meltano.generation import (
    load_assets_from_meltano_project,
    load_jobs_from_meltano_project,
)
from dagster_meltano.meltano_resource import MeltanoResource, meltano_resource
