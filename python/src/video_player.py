"""A video player class."""
import random

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.isPlaying = False
        self.titlePlaying = ""

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

    def show_all_videos(self):
        """Returns all videos."""
      #  allVideos = self._video_library.get_all_videos()
       # allVideos.sort()
        allVideos = self.sortListOfVideos()
        for video in allVideos:
            tagString = ' '.join(video.tags)
            print("{0} ({1}) [{2}]".format(video.title, video.video_id, tagString))

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
            self.setTitlePlaying(playingVideo.title)
            print("Playing video: {}".format(self.titlePlaying))
        else:
            if self.titlePlaying != playingVideo.title:
                print("Stopping video: {}".format(self.titlePlaying))
                self.setTitlePlaying(playingVideo.title)
                print("Playing video: {}".format(self.titlePlaying))
            else:
                print("Stopping video: {}".format(self.titlePlaying))
                print("Playing video: {}".format(self.titlePlaying))



    def setIsPlaying(self, isPlaying):
        """
        Set isPlaying property to either True or False
        :param isPlaying: boolean
        """
        self.isPlaying = isPlaying

    def setTitlePlaying(self, aTitle):
        """
        Sets the value of the attribute titlePlaying
        :param aTitle:
        :return: none
        """
        self.titlePlaying = aTitle


    def stop_video(self):
        """Stops the current video."""
        if self.isPlaying:
            print("Stopping video: {}".format(self.titlePlaying))
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

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

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
