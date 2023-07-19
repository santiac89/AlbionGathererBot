from enum import Enum
from events.mount_event import MountEvent
from operations.mount_start_operation import MountStartOperation
from bot import Bot
from events.albion_events import AlbionEvents
from events.harvesting_finished_event import HarvestingFinishedEvent
from operations.mount_start_operation import MountStartOperation
from operations.albion_operation_codes import AlbionOperationCodes
from operations.join_operation import JoinOperation
from operations.move_operation import MoveOperation

class AlbionEventsHandler:
    def __init__(self, bot: Bot):
        self._event_handlers = []
        self._operation_handlers = []
        self._bot = bot
        self._userId = -1

    def on_event(self, event):
        event_code = self.parse_event_code(event.parameters)

        if event_code <= -1:
            return

        if AlbionEvents.has_value(event_code):
            event_code = AlbionEvents(event_code)
            
            if event_code == AlbionEvents.NewPortalEntrance:
                print("New portal entrance")
            
            if 0 in event.parameters and event.parameters[0] == self._userId:
                if event_code == AlbionEvents.HarvestFinished:
                    event = HarvestingFinishedEvent(event.parameters)
                    self._bot.on_harvest_finished(event)
                elif event_code == AlbionEvents.HealthUpdate:
                    self._bot.on_health_update()
                elif event_code == AlbionEvents.Mount: # NOTE: Fix this
                    event = MountEvent(event.parameters)
                    self._bot.on_mount(event)

    def on_request(self, request):
        operation_code = self.parse_operation_code(request.parameters)

        if operation_code <= -1:
            return

        if AlbionOperationCodes.has_value(operation_code):
            if 0 in request.parameters:
                operation_code = AlbionOperationCodes(operation_code)

                if operation_code == AlbionOperationCodes.Move:
                    move_operation = MoveOperation(request.parameters)
                    self._bot.on_move(move_operation)
                elif operation_code == AlbionOperationCodes.HarvestStart:
                    self._bot.on_harvest_started()
                elif operation_code == AlbionOperationCodes.MountStart:
                    mount_operation = MountStartOperation(request.parameters)
                elif operation_code == AlbionOperationCodes.Join:
                    join = JoinOperation(request.parameters)
                    self._userId = join.UserObjectId

    def on_response(self, response):
        operation_code = self.parse_operation_code(response.parameters)

        if operation_code <= -1:
            return

    def parse_operation_code(self, parameters):
        if 253 not in parameters:
            return -1

        return parameters[253]

    def parse_event_code(self, parameters):
        if 252 not in parameters:
            return -1

        return parameters[252]