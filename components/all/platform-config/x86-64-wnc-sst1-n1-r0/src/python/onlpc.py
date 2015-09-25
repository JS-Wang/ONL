#!/usr/bin/python
############################################################
# <bsn.cl fy=2013 v=none>
#
#        Copyright 2013, 2014 BigSwitch Networks, Inc.
#
#
#
# </bsn.cl>
############################################################
#
# Platform driver for the WNC
#
############################################################
import subprocess
from onl.platform.base import *
from onl.vendor.wnc import *


class OpenNetworkPlatformImplementation(OpenNetworkPlatformWnc):

    def model(self):
        return "WNC-SST1-N1"

    def platform(self):
        return "x86-64-wnc-sst1-n1-r0"

    def _plat_info_dict(self):
        return {
            platinfo.LAG_COMPONENT_MAX : 24,
            platinfo.PORT_COUNT : 54,
            platinfo.ENHANCED_HASHING : True,
            platinfo.SYMMETRIC_HASHING : True,
            }

    def sys_init(self):
        pass

    def sys_oid_platform(self):
        return ".1.1"

if __name__ == "__main__":
    print OpenNetworkPlatformImplementation()

