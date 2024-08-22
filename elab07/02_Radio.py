class Radio():
    def __init__(self, mode="FM", frequency=87.5):
        self.mode = mode
        self.frequency = frequency

    def __str__(self):
        if self.get_mode() == 'FM':
            return f"{self.get_mode()} Radio: {self.get_frequency():.1f} MHz"
        else:
            return f"{self.get_mode()} Radio: {self.get_frequency():.1f} kHz"
    
    def set_mode(self, mode):
        self.mode = mode
        if mode == 'FM':
            self.frequency = 87.5
        elif mode == 'AM':
            self.frequency = 150
    
    def set_frequency(self, frequency):
        if self.mode == 'FM':
            if frequency >= 87.5 and frequency <= 108:
                self.frequency = frequency
        elif self.mode == 'AM':
            if frequency >= 150 and frequency <= 280:
                self.frequency = frequency

    def get_mode(self):
        return self.mode
    
    def get_frequency(self):
        return self.frequency
    
    def adjust_frequency(self, frequency):
        if self.mode == 'FM':
            if self.frequency + frequency >= 87.5 and self.frequency + frequency <= 108:
                self.frequency += frequency
                return True
        elif self.mode == 'AM':
            if self.frequency + frequency >= 150 and self.frequency + frequency <= 280:
                self.frequency += frequency
                return True
        return False