# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6207, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class Enum0(str, Enum):
    
    applicationjsonodatanometadata = "application/json;odata=nometadata"
    applicationjsonodataminimalmetadata = "application/json;odata=minimalmetadata"
    applicationjsonodatafullmetadata = "application/json;odata=fullmetadata"

class GeoReplicationStatusType(str, Enum):
    
    live = "live"
    bootstrap = "bootstrap"
    unavailable = "unavailable"