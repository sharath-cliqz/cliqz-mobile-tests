class TestFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class ScriptFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class OnboardingFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class FreshTabFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class TopBarFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class TabsOverviewFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class ReaderModeError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class AlertBoxFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class DeviceTypeFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class GeckoFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class SettingsFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class GhosteryCCFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class GeckoFailure(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value