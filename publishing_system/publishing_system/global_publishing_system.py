class GlobalPublishingSystem:
    SYSTEM = None

    @classmethod
    def get_system(cls):
        return cls.SYSTEM

    @classmethod
    def set_system(cls, new_system):
        cls.SYSTEM = new_system
