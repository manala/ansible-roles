#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: files_attributes
author: Manala (@manala)
short_description: Manage files attributes
description: Manage files attributes
'''

EXAMPLES = r'''
- name: Touch file
  manala.roles.files_attributes:
    path: /tmp/touch
    state: touch
'''
