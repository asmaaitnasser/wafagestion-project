"""
Helper to import backend modules
Handles different import scenarios for development and deployment
"""

import sys
from pathlib import Path


def setup_backend_path():
    """Add backend to Python path"""
    project_root = Path(__file__).parent.parent.parent
    backend_path = project_root / "backend"
    backend_src_path = project_root / "backend" / "src"

    # Add to path if not already there
    for path in [str(project_root), str(backend_path), str(backend_src_path)]:
        if path not in sys.path:
            sys.path.insert(0, path)


def import_portfolio_reconstructor():
    """Import PortfolioReconstructor with fallback"""
    setup_backend_path()

    try:
        from backend.src.api.wrapper import PortfolioReconstructor
        return PortfolioReconstructor
    except ImportError:
        pass

    try:
        from api.wrapper import PortfolioReconstructor
        return PortfolioReconstructor
    except ImportError:
        pass

    # Last resort: direct import
    import importlib.util
    project_root = Path(__file__).parent.parent.parent
    wrapper_path = project_root / "backend" / "src" / "api" / "wrapper.py"

    spec = importlib.util.spec_from_file_location("wrapper", wrapper_path)
    wrapper_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(wrapper_module)

    return wrapper_module.PortfolioReconstructor


def import_ml_predictor():
    """Import MLPredictor with fallback"""
    setup_backend_path()

    try:
        from backend.src.api.wrapper import MLPredictor
        return MLPredictor
    except ImportError:
        pass

    try:
        from api.wrapper import MLPredictor
        return MLPredictor
    except ImportError:
        pass

    # Last resort: direct import
    import importlib.util
    project_root = Path(__file__).parent.parent.parent
    wrapper_path = project_root / "backend" / "src" / "api" / "wrapper.py"

    spec = importlib.util.spec_from_file_location("wrapper", wrapper_path)
    wrapper_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(wrapper_module)

    return wrapper_module.MLPredictor
