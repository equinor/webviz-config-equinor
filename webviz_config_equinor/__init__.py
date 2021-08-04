import os
import glob
from pkg_resources import get_distribution, DistributionNotFound

from webviz_config import WebvizConfigTheme
from plotly import colors

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass


equinor_theme = WebvizConfigTheme(theme_name="equinor")
equinor_alt1_theme = WebvizConfigTheme(theme_name="equinor-alt1")
equinor_alt2_theme = WebvizConfigTheme(theme_name="equinor-alt2")

for theme in [equinor_theme, equinor_alt1_theme, equinor_alt2_theme]:
    theme.external_stylesheets = [
        "https://eds-static.equinor.com/font/equinor-font.css"
    ]

    theme.adjust_csp(
        {
            "font-src": ["https://eds-static.equinor.com"],
            "img-src": ["https://eds-static.equinor.com"],
            "style-src": ["https://eds-static.equinor.com"],
        },
        append=True,
    )

    theme.assets = glob.glob(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "*")
    )

    theme.plotly_theme = {
        "layout": {
            "font": {"family": "Equinor"},
            "hoverlabel": {"font": {"family": "Equinor"}},
            "plot_bgcolor": "white",
            "xaxis": {"exponentformat": "SI"},
            "yaxis": {"exponentformat": "SI"},
            "coloraxis": {"colorbar": {"exponentformat": "SI"}},
        }
    }

equinor_plotly_theme = equinor_theme.plotly_theme
equinor_plotly_theme["layout"].update(
    {
        "colorscale": {
            "diverging": [
                [0, "rgb(255, 18, 67)"],
                [0.1, "rgb(36, 55, 70)"],
                [0.2, "rgb(0, 112, 121)"],
                [0.3, "rgb(213, 234, 244)"],
                [0.4, "rgb(230, 250, 236)"],
                [0.5, "rgb(255, 231, 214)"],
                [0.6, "rgb(128, 183, 188)"],
                [0.7, "rgb(255, 18, 67)"],
                [0.8, "rgb(145, 155, 162)"],
                [0.9, "rgb(190, 128, 145)"],
                [1, "rgb(178, 212, 215)"],
            ],
            "sequential": [
                [0.0, "rgb(36, 55, 70)"],
                [0.125, "rgb(102, 115, 125)"],
                [0.25, "rgb(145, 155, 162)"],
                [0.375, "rgb(189, 195, 199)"],
                [0.5, "rgb(255, 231, 214)"],
                [0.625, "rgb(216, 178, 189)"],
                [0.75, "rgb(190, 128, 145)"],
                [0.875, "rgb(164, 76, 101)"],
                [1.0, "rgb(125, 0, 35)"],
            ],
        },
        "colorway": [
            "#FF1243",
            "#243746",
            "#007079",
            "#80B7BC",
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
    }
)
equinor_theme.plotly_theme = equinor_plotly_theme

equinor_alt1_plotly_theme = equinor_alt1_theme.plotly_theme
equinor_alt1_plotly_theme["layout"].update(
    {
        "colorscale": {
            "diverging": colors.get_colorscale("piyg"),
            "sequential": colors.get_colorscale("plotly3"),
        },
        "colorway": colors.qualitative.Plotly,
    }
)
equinor_alt1_theme.plotly_theme = equinor_alt1_plotly_theme

equinor_alt2_plotly_theme = equinor_alt2_theme.plotly_theme
equinor_alt2_plotly_theme["layout"].update(
    {
        "colorscale": {
            "diverging": colors.get_colorscale("spectral"),
            "sequential": colors.get_colorscale("viridis"),
        },
        "colorway": colors.qualitative.D3,
    }
)
equinor_alt2_theme.plotly_theme = equinor_alt2_plotly_theme
