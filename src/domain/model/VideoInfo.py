class VideoInfo:
    def __init__(self, name: str, frames: int, width: int, height: int):
        self.name = name
        self.frames = frames
        self.width = width
        self.height = height

    def __str__(self):
        return f"VideoInfo(name={self.name}, frames={self.frames}, width={self.width}, height={self.height})"

    def __repr__(self):
        return self.__str__()
