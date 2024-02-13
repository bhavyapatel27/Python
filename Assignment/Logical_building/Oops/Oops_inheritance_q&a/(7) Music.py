class MusicalInstrument:
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def play(self):
        print(f"The {self.name} makes a {self.sound} sound.")


class StringInstrument(MusicalInstrument):
    def __init__(self, name, type, sound, num_strings):
        super().__init__(name, type, sound)
        self.num_strings = num_strings

    def play(self):
        super().play()
        print(f"It has {self.num_strings} strings.")

violin = StringInstrument("Violin", "String", "bright", 4)
violin.play()


class WindInstrument(MusicalInstrument):
    def __init__(self, name, type, sound, material):
        super().__init__(name, type, sound)
        self.material = material

    def play(self):
        super().play()
        print(f"It is made of {self.material}.")

trumpet = WindInstrument("Trumpet", "Brass", "loud", "brass")
trumpet.play()


class PercussionInstrument(MusicalInstrument):
    def __init__(self, name, type, sound, material):
        super().__init__(name, type, sound)
        self.material = material

    def play(self):
        super().play()
        print(f"It is made of {self.material}.")

drum = PercussionInstrument("Drum", "Percussion", "booming", "wood")
drum.play()
