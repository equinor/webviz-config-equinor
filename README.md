[![PyPI version](https://badge.fury.io/py/webviz-config-equinor.svg)](https://badge.fury.io/py/webviz-config-equinor)
[![Build Status](https://github.com/equinor/webviz-config-equinor/workflows/webviz-config-equinor/badge.svg)](https://github.com/equinor/webviz-config-equinor/actions?query=branch%3Amaster)
[![Python 3.8 | 3.9](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8%20|%203.9%20|%203.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

# Webviz config theme for Equinor

Enables Equinor theme for Webviz applications build through `webviz-config`.

The simplest way of installing `webviz-config-equinor` is to run
```bash
pip install webviz-config-equinor
```

If you want to download the latest source code and install it manually you 
can run
```bash
git clone git@github.com:equinor/webviz-config-equinor.git
cd webviz-config-equinor
pip install .
```

After installation you can enable the Equinor theme by e.g.
```bash
webviz build your_config.yaml --theme equinor
```

# Terms and conditions

This repository, both as a whole and individual files,
are fully owned by Equinor.

All rights reserved.

You are allowed to install and store the content on your computer, but only
for your own personal testing in an `webviz` application. Non-personal
and public usage requires approval by Equinor.

You are allowed to use the overall structure as a guide on how to
create a new `webviz` theme, but all references to Equinor should
be removed in your new theme.

Any other kind of use, reproduction, translation, adaptation, arrangement,
any other alteration, distribution or storage of this repository in any
form and by any means, in whole or in part, without the prior written
permission of Equinor is prohibited.

Neither Equinor nor any of its subsidiaries accept liability for any direct,
indirect, special, substantial or other losses or damage of whatsoever kind
arising from access to, or the use of this repository or any
information contained in it.

This notice shall be governed by and construed in accordance with Norwegian law.

If any provision of this notice shall be unlawful, void or for any reason
unenforceable then that provision shall be deemed severable and shall not
affect the validity and enforcability of the remaining provisions.
