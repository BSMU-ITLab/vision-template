"""
See build instructions:
https://github.com/BSMU-ITLab/vision/blob/main/scripts/build.py
"""

from pathlib import Path

from bsmu.vision.app.builder import AppBuilder

import orgname.template
from orgname.template.app import TemplateApp


if __name__ == '__main__':
    app_builder = AppBuilder(
        project_dir=Path(__file__).resolve().parents[1],
        app_class=TemplateApp,

        script_path_relative_to_project_dir=Path('src/orgname/template/app/__main__.py'),
        icon_path_relative_to_project_dir=Path('src/orgname/template/app/images/icons/vision.ico'),

        add_packages=['orgname.template', 'scipy.optimize', 'scipy.integrate'],
        add_packages_with_data=[orgname.template],
    )
    app_builder.build()
