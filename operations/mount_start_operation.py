class MountStartOperation():
    def __init__(self, parameters):
        self.mounted = parameters[2] if 2 in parameters else False
        self.fast_mounted = parameters[3] if 3 in parameters else False