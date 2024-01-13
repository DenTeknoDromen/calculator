# Class for storing and showing input from/to GUI
class input:
    def __init__(self) -> None:
        self.main_str = ""
        self.lst_input = []
        self.font_size = 41
    
    def reset(self):
        self.main_str = ""
        self.font_size = 41

    def reset_font(self):
        self.font_size = 41

