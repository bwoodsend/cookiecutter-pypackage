# -*- coding: utf-8 -*-
"""
Freeze pytest.main() with {{ cookiecutter.project_slug }} included.
"""
import {{ cookiecutter.project_slug }}

import pytest
pytest.main()
