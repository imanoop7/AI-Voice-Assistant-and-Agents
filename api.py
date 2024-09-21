import enum
from typing import Annotated
from livekit.agents import llm
import logging

logger = logging.getLogger("temprature-control")
logger.setLevel(logging.INFO)


class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"



class AssistantFuc(llm.FunctionContext):
    def __init__(self) -> None:
        super().__init__()

        self ._temprature={
            Zone.LIVING_ROOM:22,
            Zone.BEDROOM:20,
            Zone.KITCHEN:24,
            Zone.BATHROOM:23,
            Zone.OFFICE:21,
        }

    @llm.ai_callable(description="get the temprature in a specific room")
    def get_temprature(self, zone:Annotated[Zone, llm.TypeInfo(description="The specific zone")]):
        logger.info("get temp- zone %s", zone)
        temp = self._temprature[Zone(zone)]
        return f"The  temprature in the {zone} is {temp}C"

