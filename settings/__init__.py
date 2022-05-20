# Copyright 2022 ITCase (info@itcase.pro)

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.absolute()

from .cache import CACHES  # noqa
from .core import *  # noqa
from .logging import LOGGING  # noqa

from .filebrowser import *  # noqa
from .grappelli import *  # noqa
from .rest_framework import REST_FRAMEWORK  # noqa
from .rq import RQ_QUEUES  # noqa

from .project import *  # noqa

from .local import *  # noqa
