from enum import auto, Enum

##last item is rendered on top 

class RenderOrder(Enum):
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()