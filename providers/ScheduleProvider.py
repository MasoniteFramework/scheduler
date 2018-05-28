''' A ScheduleProvider Service Provider '''
from masonite.provider import ServiceProvider
from ..commands.ScheduleRunCommand import ScheduleRunCommand

class ScheduleProvider(ServiceProvider):

    def register(self):
        self.app.bind('ScheduleCommand', ScheduleRunCommand())

    def boot(self):
        pass
