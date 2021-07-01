#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""A command parser class."""

import textwrap
from typing import Sequence


class CommandException(Exception):
    """A class used to represent a wrong command exception."""
    pass


class CommandParser:
    """A class used to parse and execute a user Command."""

    def __init__(self, video_player):
        self._player = video_player

    def execute_command(self, command: Sequence[str]):
        """Executes the user command. Expects the command to be upper case.
           Raises CommandException if a command cannot be parsed.
        """
        if not command:
            raise CommandException(
                "Please enter a valid command, "
                "type HELP for a list of available commands.")

        if command[0].upper() == "NUMBER_OF_VIDEOS":
            self._player.number_of_videos()

        elif command[0].upper() == "SHOW_ALL_VIDEOS":
            self._player.show_all_videos()

        elif command[0].upper() == "PLAY":
            if len(command) != 2:
                raise CommandException(
                    "Please enter PLAY command followed by video_id.")
            self._player.play_video(command[1])

        elif command[0].upper() == "PLAY_RANDOM":
            self._player.play_random_video()

        elif command[0].upper() == "STOP":
            self._player.stop_video()

        elif command[0].upper() == "PAUSE":
            self._player.pause_video()

        elif command[0].upper() == "CONTINUE":
            self._player.continue_video()

        elif command[0].upper() == "SHOW_PLAYING":
            self._player.show_playing()

        elif command[0].upper() == "CREATE_PLAYLIST":
            if len(command) != 2:
                raise CommandException(
                    "Please enter CREATE_PLAYLIST command followed by a "
                    "playlist name.")
            self._player.create_playlist(command[1])

        elif command[0].upper() == "ADD_TO_PLAYLIST":
            if len(command) != 3:
                raise CommandException(
                    "Please enter ADD_TO_PLAYLIST command followed by a "
                    "playlist name and video_id to add.")
            self._player.add_to_playlist(command[1], command[2])

        elif command[0].upper() == "REMOVE_FROM_PLAYLIST":
            if len(command) != 3:
                raise CommandException(
                    "Please enter REMOVE_FROM_PLAYLIST command followed by a "
                    "playlist name and video_id to remove.")
            self._player.remove_from_playlist(command[1], command[2])

        elif command[0].upper() == "CLEAR_PLAYLIST":
            if len(command) != 2:
                raise CommandException(
                    "Please enter CLEAR_PLAYLIST command followed by a "
                    "playlist name.")
            self._player.clear_playlist(command[1])

        elif command[0].upper() == "DELETE_PLAYLIST":
            if len(command) != 2:
                raise CommandException(
                    "Please enter DELETE_PLAYLIST command followed by a "
                    "playlist name.")
            self._player.delete_playlist(command[1])

        elif command[0].upper() == "SHOW_PLAYLIST":
            if len(command) != 2:
                raise CommandException(
                    "Please enter SHOW_PLAYLIST command followed by a "
                    "playlist name.")
            self._player.show_playlist(command[1])

        elif command[0].upper() == "SHOW_ALL_PLAYLISTS":
            self._player.show_all_playlists()

        elif command[0].upper() == "SEARCH_VIDEOS":
            if len(command) != 2:
                raise CommandException(
                    "Please enter SEARCH_VIDEOS command followed by a "
                    "search term.")
            self._player.search_videos(command[1])

        elif command[0].upper() == "SEARCH_VIDEOS_WITH_TAG":
            if len(command) != 2:
                raise CommandException(
                    "Please enter SEARCH_VIDEOS_WITH_TAG command followed by a "
                    "video tag.")
            self._player.search_videos_tag(command[1])

        elif command[0].upper() == "FLAG_VIDEO":
            if len(command) == 3:
                self._player.flag_video(command[1], command[2])
            elif len(command) == 2:
                self._player.flag_video(command[1])
            else:
                raise CommandException(
                    "Please enter FLAG_VIDEO command followed by a "
                    "video_id and an optional flag reason.")

        elif command[0].upper() == "ALLOW_VIDEO":
            if len(command) != 2:
                raise CommandException(
                    "Please enter ALLOW_VIDEO command followed by a "
                    "video_id.")
            self._player.allow_video(command[1])

        elif command[0].upper() == "HELP":
            self._get_help()
        else:
            print(
                "Please enter a valid command, type HELP for a list of "
                "available commands.")

    def _get_help(self):
        """Displays all available commands to the user."""
        help_text = textwrap.dedent("""
        Available commands:
            NUMBER_OF_VIDEOS - Shows how many videos are in the library.
            SHOW_ALL_VIDEOS - Lists all videos from the library.
            PLAY <video_id> - Plays specified video.
            PLAY_RANDOM - Plays a random video from the library.
            STOP - Stop the current video.
            PAUSE - Pause the current video.
            CONTINUE - Resume the current paused video.
            SHOW_PLAYING - Displays the title, url and paused status of the video that is currently playing (or paused).
            CREATE_PLAYLIST <playlist_name> - Creates a new (empty) playlist with the provided name.
            ADD_TO_PLAYLIST <playlist_name> <video_id> - Adds the requested video to the playlist.
            REMOVE_FROM_PLAYLIST <playlist_name> <video_id> - Removes the specified video from the specified playlist
            CLEAR_PLAYLIST <playlist_name> - Removes all the videos from the playlist.
            DELETE_PLAYLIST <playlist_name> - Deletes the playlist.
            SHOW_PLAYLIST <playlist_name> - List all the videos in this playlist.
            SHOW_ALL_PLAYLISTS - Display all the available playlists.
            SEARCH_VIDEOS <search_term> - Display all the videos whose titles contain the search_term.
            SEARCH_VIDEOS_WITH_TAG <tag_name> -Display all videos whose tags contains the provided tag.
            FLAG_VIDEO <video_id> <flag_reason> - Mark a video as flagged.
            ALLOW_VIDEO <video_id> - Removes a flag from a video.
            HELP - Displays help.
            EXIT - Terminates the program execution.
        """)
        print(help_text)


# In[22]:


"""A youtube terminal simulator."""
get_ipython().run_line_magic('pip', 'install VideoPlayer')
get_ipython().run_line_magic('pip', 'install CommandException')
get_ipython().run_line_magic('pip', 'install CommandParser')

if __name__ == "__main__":
    print("""Hello and welcome to YouTube, what would you like to do?
    Enter HELP for list of available commands or EXIT to terminate.""")
    video_player = VideoPlayer()
    parser = CommandParser(video_player)
    while True:
        command = input("YT> ")
        if command.upper() == "EXIT":
            break
        try:
            parser.execute_command(command.split())
        except CommandException as e:
            print(e)
    print("YouTube has now terminated its execution. "
          "Thank you and goodbye!")


# In[12]:


"""A video class."""

from typing import Sequence

class FlagError(Exception):
    pass

class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)
        # When the flag reason is None it means the video is not flagged
        # This allows us to not need a self._is_flagged.
        self._flag_reason = None

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    @property
    def tags_string(self) -> str:
        """Returns the tags as a string, like "#cat #animal"
        separated by spaces"""
        return ' '.join(self.tags)

    def __str__(self):
        """This function prints the video when you do print(video) like
        Amazing Cats (amazing_cats_video_id) [#cat #animal]
        """
        result = f'{self.title} ({self.video_id}) [{self.tags_string}]'
        if self.is_flagged:
            result += f' - FLAGGED {self.formatted_flag_reason}'
        return result

    def flag(self, flag_reason: str):
        if self.is_flagged:
            raise FlagError("Video is already flagged")
        self._flag_reason = flag_reason

    def unflag(self):
        if not self.is_flagged:
            raise FlagError("Video is not flagged")
        self._flag_reason = None

    @property
    def is_flagged(self):
        """Return True if the flag reason is not None"""
        return self._flag_reason is not None

    def check_allowed(self):
        """Return True if the video is not currently flagged"""
        if self.is_flagged:
            raise FlagError(f"Video is currently flagged {self.formatted_flag_reason}")

    @property
    def formatted_flag_reason(self):
        """Format the flag reason properly. If it's not flagged we can
        return an empty string."""
        if self.is_flagged:
            return f'(reason: {self._flag_reason})'
        else:
            return ''


# In[14]:


"""A video library class."""

from typing import Sequence, Optional

import csv
import random
from pathlib import Path

get_ipython().run_line_magic('pip', 'install Video')


# Helper Wrapper around CSV reader to strip whitespace from around
# each item.
def _csv_reader_with_strip(reader):
    yield from ((item.strip() for item in line) for line in reader)


class VideoLibraryError(Exception):
    pass


class VideoLibrary:
    """A class used to represent a Video Library."""

    def __init__(self):
        """The VideoLibrary class is initialized."""
        self._videos = {}
        with open(Path(__file__).parent / "videos.txt") as video_file:
            reader = _csv_reader_with_strip(
                csv.reader(video_file, delimiter="|"))
            for video_info in reader:
                title, url, tags = video_info
                self._videos[url] = Video(
                    title,
                    url,
                    [tag.strip() for tag in tags.split(",")] if tags else [],
                )

    def get_all_videos(self) -> Sequence[Video]:
        """Returns all available video information from the video library."""
        return list(sorted(self._videos.values(), key=str))

    def get_allowed_videos(self) -> Sequence[Video]:
        """Returns all allowed videos in the library."""
        return [v for v in self.get_all_videos() if not v.is_flagged]

    def __getitem__(self, video_id):
        """This is a way to make the Video library behave like a python
        dictionary. So now we can do video_library[video_id] and it will
        return the video if it exists ot throw a VideoLibraryError.
        See also: https://www.kite.com/python/answers/how-to-override-the-[]-operator-in-python
        """
        try:
            return self._videos[video_id]
        except KeyError:
            raise VideoLibraryError("Video does not exist")

    def get_video(self, video_id: str) -> Optional[Video]:
        """Returns the video object (title, url, tags) from the video library.
        Args:
            video_id: The video url.
        Returns:
            The Video object for the requested video_id. None if the video
            does not exist.
        """
        return self._videos.get(video_id, None)

    def get_random_video_id(self) -> Optional[str]:
        """Returns a Random Video id from the list of allowed videos.
        If there are no videos available (e.g. all of them are flagged or
        something else happened) we return None.
        """
        try:
            return random.choice([video.video_id for video in self.get_allowed_videos()])
        except IndexError:
            return None

    def search_videos(self, search_term: str):
        """Search through all the titles (in lower case) and return if the title
        contains the search term."""
        search_term = search_term.lower()
        return [v for v in self.get_allowed_videos() if search_term in v.title.lower()]

    def get_videos_with_tag(self, tag: str):
        """Search through all the tags and return all videos whose tags
        contain the search tag."""
        return [v for v in self.get_allowed_videos() if tag in v.tags]


# In[15]:


import enum

class VideoPlaybackError(Exception):
    pass


class PlaybackState(enum.Enum):
    STOPPED = 0
    PAUSED = 1
    PLAYING = 2


class VideoPlayback:
    """A class to keep track of the currently playing video and it's state
    (PAUSED, STOPPED, PLAYING).
    We need to make sure we keep the two together because when no video is
    currently playing, it can also not be paused.
    """
    def __init__(self):
        self._video = None
        self._state = PlaybackState.STOPPED

    def play(self, video):
        self._video = video
        self._state = PlaybackState.PLAYING

    def pause(self):
        self._check_video()
        self._state = PlaybackState.PAUSED

    def resume(self):
        self._check_video()

        if self._state != PlaybackState.PAUSED:
            raise VideoPlaybackError("Video is not paused")

        self._state = PlaybackState.PLAYING

    def stop(self):
        self._check_video()
        self._video = None
        self._state = PlaybackState.STOPPED

    def get_video(self):
        self._check_video()
        return self._video

    @property
    def state(self):
        return self._state

    def _check_video(self):
        """Check to make sure that there is a video currently playing."""
        if self._video is None:
            raise VideoPlaybackError("No video is currently playing")


# In[19]:


"""A video player class."""

import random
from .video_library import VideoLibrary, VideoLibraryError
from . import video_playlist_library
from .video import FlagError
from .video_playlist import VideoPlaylistError
from .video_playlist_library import VideoPlaylistLibraryError
from .video_playback import VideoPlayback, VideoPlaybackError, PlaybackState


class VideoPlayerError(Exception):
    pass


def _print_video_choice_list(videos):
    for i, video in enumerate(videos, start=1):
        print(f"  {i}) {video})")

    print("Would you like to play any of the above? If yes, specify the number of the video.")
    print("If your answer is not a valid number, we will assume it's a no.")

    user_input = input("")

    try:
        num = int(user_input)
    except ValueError:
        num = 0

    if 1 <= num <= len(videos):
        return videos[num - 1]
    else:
        return None


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        """The VideoPlayer class is initialized."""
        self._videos = VideoLibrary()
        self._playlists = video_playlist_library.VideoPlaylistLibrary()
        self._playback = VideoPlayback()


    def number_of_videos(self):
        num_videos = len(self._videos.get_all_videos())
        print(f"{num_videos} videos in the library")


    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        for v in self._videos.get_all_videos():
            print(v)

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """

        try:
            video = self._videos[video_id]
            video.check_allowed()
        except (VideoLibraryError, FlagError) as e:
            print(f"Cannot play video: {e}")
            return

        if self._playback.state != PlaybackState.STOPPED:
            self.stop_video()
        self._playback.play(video)
        print(f"Playing video: {video.title}")

    def stop_video(self):
        """Stops the current video."""

        try:
            video = self._playback.get_video()
            print(f"Stopping video: {video.title}")
            self._playback.stop()
        except VideoPlaybackError as e:
            print(f"Cannot stop video: {e}")

    def play_random_video(self):
        """Plays a random video from the video library."""

        random_video_id = self._videos.get_random_video_id()

        if random_video_id is None:
            print("No videos available")
        else:
            self.play_video(random_video_id)

    def pause_video(self):
        """Pauses the current video."""

        try:
            video = self._playback.get_video()
        except VideoPlaybackError as e:
            print(f"Cannot pause video: {e}")
            return

        if self._playback.state == PlaybackState.PAUSED:
            print(f"Video already paused: {video.title}")
            return

        print(f"Pausing video: {video.title}")
        self._playback.pause()

    def continue_video(self):
        """Resumes playing the current video."""

        try:
            video = self._playback.get_video()
            self._playback.resume()
            print(f"Continuing video: {video.title}")
        except VideoPlaybackError as e:
            print(f"Cannot continue video: {e}")

    def show_playing(self):
        """Displays video currently playing."""

        if self._playback.state == PlaybackState.PLAYING:
            print(f"Currently playing: {self._playback.get_video()}")
        elif self._playback.state == PlaybackState.PAUSED:
            print(f"Currently playing: {self._playback.get_video()} - PAUSED")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """

        try:
            self._playlists.create(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")
        except VideoPlaylistLibraryError as e:
            print(f"Cannot create playlist: {e}")            

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        try:
            playlist = self._playlists[playlist_name]
            video = self._videos[video_id]
            video.check_allowed()
            playlist.add_video(video)
            print(f"Added video to {playlist_name}: {video.title}")
        except (VideoPlaylistLibraryError, VideoPlaylistError, VideoLibraryError, FlagError) as e:
            print(f"Cannot add video to {playlist_name}: {e}")

    def show_all_playlists(self):
        """Display all playlists."""

        playlists = list(self._playlists.get_all())

        if not playlists:
            print("No playlists exist yet")
            return

        print("Showing all playlists:")
        for playlist in playlists:
            print(f"  {playlist}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """

        try:        
            playlist = self._playlists[playlist_name]
        except VideoPlaylistLibraryError as e:
            print(f"Cannot show playlist {playlist_name}: {e}")
            return

        print(f"Showing playlist: {playlist_name}")

        if not playlist.videos:
            print("No videos here yet")
            return

        for video in playlist.videos:
            print(f"  {video}")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        try:
            playlist = self._playlists[playlist_name]
            video = self._videos[video_id]
            playlist.remove_video(video)
            print(f"Removed video from {playlist_name}: {video.title}")
        except (VideoPlaylistError, VideoLibraryError, VideoPlaylistLibraryError) as e:
            print(f"Cannot remove video from {playlist_name}: {e}")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """

        try:        
            playlist = self._playlists[playlist_name]
            playlist.clear()
            print(f"Successfully removed all videos from {playlist_name}")
        except (VideoPlaylistError, VideoPlaylistLibraryError) as e:
            print(f"Cannot clear playlist {playlist_name}: {e}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """

        try:        
            playlist = self._playlists[playlist_name]
            del self._playlists[playlist_name]
            print(f"Deleted playlist: {playlist_name}")
        except VideoPlaylistLibraryError as e:
            print(f"Cannot delete playlist {playlist_name}: {e}")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search.
        """
        
        results = self._videos.search_videos(search_term)

        if not results:
            print(f"No search results for {search_term}")
            return

        print(f"Here are the results for {search_term}:")
        chosen_video = _print_video_choice_list(results)

        if chosen_video is not None:
            self.play_video(chosen_video.video_id)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.
        Args:
            video_tag: The video tag to be used in search.
        """

        results = self._videos.get_videos_with_tag(video_tag)

        if not results:
            print(f"No search results for {video_tag}")
            return

        print(f"Here are the results for {video_tag}:")
        chosen_video = _print_video_choice_list(results)

        if chosen_video is not None:
            self.play_video(chosen_video.video_id)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.
        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """

        if not flag_reason:
            flag_reason = "Not supplied"

        try:
            video = self._videos[video_id]

            if self._playback.state != PlaybackState.STOPPED and self._playback.get_video() == video:
                self.stop_video()

            video.flag(flag_reason)
            print(f"Successfully flagged video: {video.title} {video.formatted_flag_reason}")
        except (VideoPlayerError, FlagError, VideoLibraryError) as e:
            print(f"Cannot flag video: {e}")

    def allow_video(self, video_id):
        """Removes a flag from a video.
        Args:
            video_id: The video_id to be allowed again.
        """

        try:
            video = self._videos[video_id]
            video.unflag()
            print(f"Successfully removed flag from video: {video.title}")
        except (VideoPlayerError, FlagError, VideoLibraryError) as e:
            print(f"Cannot remove flag from video: {e}")


# In[20]:


"""A video playlist class."""

class VideoPlaylistError(Exception):
    pass


class VideoPlaylist:
    """A class used to represent a Playlist."""

    def __init__(self, name:str):
        self._name = name
        # Keep the videos as a list
        self._videos = []

    @property
    def name(self):
        return self._name

    @property
    def videos(self):
        return tuple(self._videos)

    def __contains__(self, video):
        """Overloading this method will allow us to use the python "in"
        operator. So now we can do `if video in playlist` like it was a list."""
        return video in self._videos

    def add_video(self, video):
        if video in self:
            raise VideoPlaylistError("Video already added")
        self._videos.append(video)

    def remove_video(self, video):
        if video not in self:
            raise VideoPlaylistError("Video is not in playlist")
        self._videos.remove(video)

    def clear(self):
        self._videos.clear()

    def __str__(self):
        """Overloading __str__ allows us to use print(..) with this object.
                When we do print(playlist) we just want to print the name."""
        return self._name


# In[ ]:


from .video_playlist import VideoPlaylist

class VideoPlaylistLibraryError(Exception):
    pass

class VideoPlaylistLibrary:
    """A library containing video playlists. We want this class to behave like
    a python dictionary but with some additional functionality.
    """
    def __init__(self):
        # keep the playlists indexed from lower-case name as key to
        # Playlist object as value. This will help us with the lookup and
        # maintaining the case.
        self._playlists = {}

    def __contains__(self, playlist_name: str):
        """Overloading __contains__ allows us to use `in` like
        `if playlist in video_library`. Here, we check if the playlist name
        in lower case is part of the playlists.
        """
        return playlist_name.lower() in self._playlists

    def create(self, playlist_name: str):
        """Create a new playlist with the provided name and store it in the
        dictionary with lowercase name for easier lookup in the future."""
        if playlist_name in self:
            raise VideoPlaylistLibraryError("A playlist with the same name already exists")
        self._playlists[playlist_name.lower()] = VideoPlaylist(playlist_name)

    def __getitem__(self, playlist_name):
        """Overloading __getitem__ will allow us to use the [] operator for
        the VideoPlaylistLibrary. e.g. we can do playlist_library[playlistname]
        to retrieve a playlist from the library.
        Here, we do the lookup in lowercase, because the playlist name should
        not be case sensitive.
        """
        try:
            return self._playlists[playlist_name.lower()]
        except KeyError:
            raise VideoPlaylistLibraryError("Playlist does not exist")

    def get(self, playlist_name, default=None):
        """Returns the playlist from the library or None if it doesn't
        exist. We look up the playlist in lowercase because we don't care
        about the case."""
        return self._playlists.get(playlist_name.lower(), default)

    def get_all(self):
        return sorted(self._playlists.values(), key=str)

    def __delitem__(self, playlist_name: str):
        """This allows us to delete a playlist from the library without
        caring about the case. """
        del self._playlists[playlist_name.lower()]

