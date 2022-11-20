class Caption:
    def __init__(self, start, end, duration, text):
        """
        Initialize the caption object
        :param start: start time of caption
        :param end: end time of caption
        :param duration: duration of caption
        :param text: text of caption
        """
        self.start = start
        self.end = end
        self.duration = duration
        self.text = text
