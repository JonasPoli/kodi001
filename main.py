# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {            '.Hack//Sekai no Mukou ni': [
                       {'name': 'Parte 03',
                       'thumb': '',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=5233b726ebe74ce5',
                       'genre': '.Hack//Sekai no Mukou ni'},

                       {'name': 'Parte 04',
                       'thumb': '',
                       'video': 'http://www.blogger.com/video-play.mp4?contentId=49107ba72fa097cd',
                       'genre': '.Hack//Sekai no Mukou ni'} ],
            '10 Things I Hate About You LEG': [
                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=4fc3fc31c5cab647',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=bc3daee00b1bd07d',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=66fe3e3f462d9bfd',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ac8ae20fc3c49d27',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ee6c48b2201677b8',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=f070031cc138ce7a',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=1a8ce3d925734901',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d058b38fce71ad9a',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=fc9477e2494d16ca',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=367bfcee532b690b',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=ddda53204cf2bfa2',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=b026c7b35f062c20',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=95f5ab7bc0e02dae',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=1b81ce86058477d5',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=d35ff38f2b423bfc',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=e9606ea35aa5c5eb',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=4f7eed42ca4c4e9e',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=29d05c0120b736a0',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=8e22220fa7bcc51f',
                       'genre': '10 Things I Hate About You LEG'},

                       {'name': '10 Things I Hate About You',
                       'thumb': 'https://ia.media-imdb.com/images/M/MV5BMmVhZjhlZDYtMDAwZi00MDcyLTgzOTItOWNiZjY0YmE0MGE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'video': 'https://www.blogger.com/video-play.mp4?contentId=7e0f197c0c78b85',
                       'genre': '10 Things I Hate About You LEG'} ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
