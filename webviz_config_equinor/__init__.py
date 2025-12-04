import glob
import importlib.metadata
import os

from plotly import colors
from webviz_config import WebvizConfigTheme

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    pass

equinor_theme = WebvizConfigTheme(theme_name="equinor")

equinor_theme.external_stylesheets = [
    "https://cdn.eds.equinor.com/font/equinor-font.css"
]

equinor_theme.adjust_csp(
    {
        "font-src": ["https://cdn.eds.equinor.com"],
        "img-src": ["https://cdn.eds.equinor.com"],
        "style-src": ["https://cdn.eds.equinor.com"],
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
