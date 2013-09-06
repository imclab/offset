# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.

from .core.util import nanotime
from .core.timer import sleep

NANOSECOND = 1
MICROSECOND = 1000 * NANOSECOND
MILLISECOND = 1000 * MICROSECOND
SECOND = 1000 * MILLISECOND
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE

nano = nanotime
sleep = sleep
