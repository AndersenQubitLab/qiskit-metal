# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
This is the main module that defines what a Base Junction, such as
a Josephson tunnel junction is.

To handle Manhatan, BFT, etc.

@author: Zlatko Minev, Thomas McConekey, ... (IBM)
@date: 2019
"""

from .base import QComponent

class BaseJunction(QComponent):
    """
    Create a new Metal junction and adds it's default_options to the design.

    Inherits QComponent class
    """
    # TODO
    pass
