import os
import glob
from pkg_resources import get_distribution, DistributionNotFound

import plotly.graph_objects as go
from webviz_config import WebvizConfigTheme


try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass

equinor_theme = WebvizConfigTheme(theme_name="equinor")

equinor_theme.external_stylesheets = [
    "https://webviz-cdn.azureedge.net/fonts/index.css",
    "https://webviz-cdn.azureedge.net/theme/equinor.theme.css",
]

equinor_theme.adjust_csp(
    {
        "style-src": ["https://webviz-cdn.azureedge.net"],
        "img-src": ["https://sibwebvizcdn.blob.core.windows.net"],
        "font-src": ["https://webviz-cdn.azureedge.net"],
    }
)

equinor_theme.assets = glob.glob(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "*")
)

equinor_theme.plotly_theme = go.layout.Template(
    layout=go.Layout(
        font =  dict(family = "Equinor"),
        hoverlabel = {"font": {"family": "Equinor"}},
        colorscale = {
            "diverging": [
                [0, "#007079"],
                [0.1, "#66737D"],
                [0.2, "#7D0023"],
                [0.3, "#4C9BA1"],
                [0.4, "#243746"],
                [0.5, "#A44C65"],
                [0.6, "#80B7BC"],
                [0.7, "#FF1243"],
                [0.8, "#919BA2"],
                [0.9, "#BE8091"],
                [1, "#B2D4D7"],
            ],
            "sequential": [
                [0.0, "#0d0887"],
                [0.1111111111111111, "#46039f"],
                [0.2222222222222222, "#7201a8"],
                [0.3333333333333333, "#9c179e"],
                [0.4444444444444444, "#bd3786"],
                [0.5555555555555556, "#d8576b"],
                [0.6666666666666666, "#ed7953"],
                [0.7777777777777778, "#fb9f3a"],
                [0.8888888888888888, "#fdca26"],
                [1.0, "#f0f921"],
            ],
            "sequentialminus": [
                [0.0, "#0d0887"],
                [0.1111111111111111, "#46039f"],
                [0.2222222222222222, "#7201a8"],
                [0.3333333333333333, "#9c179e"],
                [0.4444444444444444, "#bd3786"],
                [0.5555555555555556, "#d8576b"],
                [0.6666666666666666, "#ed7953"],
                [0.7777777777777778, "#fb9f3a"],
                [0.8888888888888888, "#fdca26"],
                [1.0, "#f0f921"],
            ],
        },
        colorway =  [
            "#007079",
            "#66737D",
            "#7D0023",
            "#4C9BA1",
            "#243746",
            "#A44C65",
            "#80B7BC",
            "#FF1243",
            "#919BA2",
            "#BE8091",
            "#B2D4D7",
            "#FF597B",
            "#BDC3C7",
            "#D8B2BD",
            "#FFE7D6",
            "#D5EAF4",
            "#FF88A1",
        ],
    )
)
