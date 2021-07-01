"""A video playlist class."""
from .video_library import VideoLibrary
from .video import Video


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self):
        self.playListName = None
        self.listOfVideos = []
        self.videoLibrary = VideoLibrary()

    def setPlayListName(self, aName):
        self.playListName = aName

    def getPlayListName(self):
        return self.playListName

    def addVideo(self, aVideo, aTitle):
       # video = self.playList.get_video(aVideo)
        self.listOfVideos.append(aVideo)
        self.listOfVideos.append(aTitle)

    def addVideoToList(self, aVideo):
        videoName = self.videoLibrary.get_video(aVideo)
        self.listOfVideos.append(videoName)

    def getVideosFromList(self):
        videoTags = []
        for video in self.listOfVideos:
            videoTags.append(video.video_id)
        return videoTags



