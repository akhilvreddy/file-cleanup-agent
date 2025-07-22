class AgentMemory:
    def __init__(self):
        self.action_log = []
        self.failures = []

    def update(self, action, result):
        if "ERROR" in result:
            self.failures.append((action, result))
        else:
            self.action_log.append((action, result))