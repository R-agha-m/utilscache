from enum import Enum


class ActionType(str,Enum):
    create = "create"
    update = "update"
    delete = "delete"
    fetch = "fetch"
