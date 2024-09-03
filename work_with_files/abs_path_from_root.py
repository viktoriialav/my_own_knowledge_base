import project_name_tests
from pathlib import Path


def abs_path_from_root(path: str):
    return Path(project_name_tests.__file__).parent.parent.joinpath(path).absolute().__str__()
