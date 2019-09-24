import os
import glob
from webviz_config.themes import WebvizConfigTheme
from pkg_resources import get_distribution, DistributionNotFound

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
