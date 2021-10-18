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

equinor_theme.external_stylesheets = [
    "https://eds-static.equinor.com/font/equinor-font.css"
]

equinor_theme.adjust_csp(
    {
        "font-src": ["https://eds-static.equinor.com"],
        "img-src": ["https://eds-static.equinor.com"],
        "style-src": ["https://eds-static.equinor.com"],
    },
    append=True,
)

equinor_theme.assets = glob.glob(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "*")
)

equinor_theme.plotly_theme = {
    "layout": {
        "font": {"family": "Equinor"},
        "hoverlabel": {"font": {"family": "Equinor"}},
        "plot_bgcolor": "white",
        "xaxis": {"exponentformat": "SI"},
        "yaxis": {"exponentformat": "SI"},
        "coloraxis": {"colorbar": {"exponentformat": "SI"}},
        "colorscale": {
            "diverging": colors.get_colorscale("spectral"),
            "sequential": colors.get_colorscale("viridis"),
        },
        "colorway": colors.qualitative.D3 + colors.qualitative.Light24,
    }
}
