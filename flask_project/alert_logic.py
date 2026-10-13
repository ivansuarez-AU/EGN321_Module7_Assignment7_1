class AlertEngine:
    def __init__(self, trigger=30.0, clear=28.5, consecutive=3):
        self.trigger=trigger
        self.clear=clear
        self.consecutive=consecutive
        self.high_count=0
        self.state="NORMAL"

    def update(self,value,valid=True):
        previous=self.state
        if not valid or value is None:
            self.high_count=0
            return self.state, previous != self.state
        if self.state=="NORMAL":
            if value >= self.trigger:
                self.high_count += 1
                if self.high_count >= self.consecutive:
                    self.state="ALERT"
            else:
                self.high_count=0
        elif self.state=="ALERT" and value <= self.clear:
            self.state="NORMAL"
            self.high_count=0
        return self.state, previous != self.state