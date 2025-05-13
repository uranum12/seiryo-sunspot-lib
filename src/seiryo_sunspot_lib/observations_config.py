from pydantic import BaseModel

from seiryo_sunspot_lib.config_common import Axis, Bar, FigSize, Title


class ObservationsMonthly(BaseModel):
    fig_size: FigSize
    bar: Bar
    title: Title
    xaxis: Axis
    yaxis: Axis
