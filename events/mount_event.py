class  MountEvent:
    def __init__(self, parameters):
        self.mounted = True if (2 in parameters) else False