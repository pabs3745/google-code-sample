"""A video player class."""
import random

from .video_library import VideoLibrary
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self.playlist = Playlist()
        self._video_library = VideoLibrary()
        self.isPlaying = False
        self.isPaused = False
        self.isStopped = False
        self.titlePlaying = ""
        self.listOfPlayList = []
        self.listOfPlaylistNames = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def sortListOfVideos(self):
        """
        Gets the list of videos, and returns them sorted
        :return: allVideos - a sorted list of videos
        """
        allVideos = self._video_library.get_all_videos()
        allVideos.sort()
        return allVideos

    def setIsPlaying(self, isPlaying):
        """
        Set isPlaying property to either True or False
        :param isPlaying: boolean
        """
        self.isPlaying = isPlaying

    def setIsPaused(self, isPaused):
        """
        Sets the variable isPaused to either true or false
        :param isPaused: boolean
        """
        self.isPaused = isPaused

    def setIsStopped(self, stop):
        """
        Sets the value of isStopped to either true or false
        :param stop: a boolean
        """
        self.isStopped = stop

    def setTitlePlaying(self, aTitle):
        """
        Sets the value of the attribute titlePlaying
        :param aTitle:
        :return: none
        """
        self.titlePlaying = aTitle

    def show_all_videos(self):
        """Returns all videos."""
        allVideos = self.sortListOfVideos()
        print("Here´s a list of all available videos:")
        for video in allVideos:
            tagString = ' '.join(video.tags)
            print("  {0} ({1}) [{2}]".format(video.title, video.video_id, tagString))

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        playingVideo = self._video_library.get_video(video_id)
        if playingVideo is None:
            print("Cannot play video: Video does not exist")
        elif not self.isPlaying:
            # videoTitle = playingVideo.title
            self.setIsPlaying(True)
            self.setIsStopped(False)
            self.setTitlePlaying(playingVideo.title)
            print("Playing video: {}".format(self.titlePlaying))
        else:
            if self.titlePlaying != playingVideo.title:
                print("Stopping video: {}".format(self.titlePlaying))
                self.setTitlePlaying(playingVideo.title)
                print("Playing video: {}".format(self.titlePlaying))
                self.setIsPaused(False)
            else:
                print("Stopping video: {}".format(self.titlePlaying))
                print("Playing video: {}".format(self.titlePlaying))
                self.setIsPaused(False)

    def stop_video(self):
        """Stops the current video."""
        if self.isPlaying:
            print("Stopping video: {}".format(self.titlePlaying))
            self.setIsPlaying(False)
            self.setIsPaused(False)
            self.setIsStopped(True)
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        allVideos = self.sortListOfVideos()
        randomNumber = random.randrange(0, len(self._video_library.get_all_videos()))
        videoId = allVideos[randomNumber].video_id
        self.play_video(videoId)

    def pause_video(self):
        """Pauses the current video."""
        if self.isPlaying is True:
            if not self.isPaused:
                self.setIsPaused(True)
                print("Pausing video: {}".format(self.titlePlaying))
            else:
                print("Video already paused: {}".format(self.titlePlaying))
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if not self.isPaused and not self.isStopped:
            print("Cannot continue video: Video is not paused")
        elif self.isStopped:
            print("Cannot continue video: No video is currently playing")
        else:
            print("Continuing video: {}".format(self.titlePlaying))
            self.setIsPaused(False)

    def show_playing(self):
        """Displays video currently playing."""
        videoPlaying = ""
        allVideos = self._video_library.get_all_videos()
        if not self.isStopped:
            for video in allVideos:
                if self.titlePlaying == video.title:
                    tagString = ' '.join(video.tags)
                    videoPlaying = "Currently playing: {0} ({1}) [{2}]".format(video.title, video.video_id, tagString)
            if self.isPaused:
                videoPlaying += " - PAUSED"
            print(videoPlaying)
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name in self.listOfPlayList:
       # if self.playlist.getPlayListName() == playlist_name:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlist.setPlayListName(playlist_name)
            print("Successfully created new playlist: {}".format(self.playlist.getPlayListName()))
            # self.listOfPlayList.append(self.playlist.getPlayListName())
            self.listOfPlaylistNames.append(self.playlist.getPlayListName())

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        videosList = list(self.sortListOfVideos())
        ids = []
        for video in videosList:
            ids.append(video.video_id)

        idsInPlayList = []
        for video in self.listOfPlayList:
            idsInPlayList.append(video.video_id)

        if playlist_name not in self.listOfPlaylistNames:
            print("Cannot add video to {}: Playlist does not exist".format(playlist_name))
        elif video_id not in ids:
            print("Cannot add video to {}: Video does not exist".format(playlist_name))
        elif video_id in idsInPlayList:
            print("Cannot add video to {}: Video already added".format(playlist_name))
        else:
            video = self._video_library.get_video(video_id)
            self.listOfPlayList.append(video)
            # self.listOfPlayList.append(video.video_id)
            print("Added video to {0}: {1}".format(self.playlist.getPlayListName(), video.title))


    def show_all_playlists(self):
        """Display all playlists."""
        if len(self.listOfPlaylistNames) < 1:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for playlist in self.listOfPlaylistNames:
                print("  {}".format(playlist))

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name in self.listOfPlaylistNames:
            print("Showing playlist: {}".format(playlist_name))
            if len(self.listOfPlayList) < 1:
                print("  No videos here yet")
            else:
                for video in self.listOfPlayList:
                    tagString = ' '.join(video.tags)
                    print("   {0} ({1}) [{2}]".format(video.title, video.video_id, tagString))
        else:
            print("Cannot show playlist {}: Playlist does not exist".format(playlist_name))


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        video = self._video_library.get_video(video_id)
        if playlist_name in self.listOfPlaylistNames:
            if video in self.listOfPlayList:
                self.listOfPlayList.remove(video)
                print("Removed video from {0}: {1}".format(playlist_name, video.title))
            else:
                print("Cannot remove video from {}: Video is not in playlist".format(playlist_name))
        else:
            print("Cannot remove video from {}: Playlist does not exist".format(playlist_name))

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("search_videos needs implementation")



    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name in self.listOfPlaylistNames:
            self.listOfPlaylistNames.remove(playlist_name)
            print("Deleted playlist: {}".format(playlist_name))
        else:
            print("Cannot delete playlist {}: Playlist does not exist".format(playlist_name))


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
