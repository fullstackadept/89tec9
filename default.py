# -*- coding: utf-8 -*-
#------------------------------------------------------------
# 89tec9 (Stretch Armstrong Show w/ Bobbito) by fullstackadept
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon and talesfromthecrypt by coldkeys
#
# Author: fullstackadept
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.89tec9'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLLOJZhtV-2tcRq1kMY63QguX4ErK-1j3Q"
YOUTUBE_CHANNEL_ID_2 = "PL6626F25BB0DDE14F"
YOUTUBE_CHANNEL_ID_3 = "PLDoXnwSn4US4WFSjpNvkLRZ0BzoQx3Cyn"
YOUTUBE_CHANNEL_ID_4 = "PLDJ4UqSFRMDn0f5JQcdJgIkUxeJZGfR5s"

# Entry point
def run():
    plugintools.log("89tec9.run")

    # Get params
    params = plugintools.get_params()

    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"

    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("89tec9.main_list "+repr(params))

    #https://i.ytimg.com/vi/TtsFwMC6Nmc/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=RZy81Sbeg7B6i1rIg7JoSRWtCQs
    plugintools.add_item(
        #action="",
        title="Full Mixshows (Stretch & Bobbito, Sway & Tech, Marley Marl & Mr. Magic, Bobby Konders)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://escobar300.files.wordpress.com/2014/03/best-radio-show-january-1998.jpg",
        fanart="https://escobar300.files.wordpress.com/2014/03/best-radio-show-january-1998.jpg",
        folder=True )

    # https://i.ytimg.com/vi/dw7Dj1wi8_A/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=G21phwQxsX6N0ed-YqP-nNFYC_U
    # https://images.rapgenius.com/6cf295d511ee87617fd3f2595e3212a7.500x262x1.jpg
    plugintools.add_item(
        #action="",
        title="Demo & Freestyles (Stretch Armstrong Show)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://1.bp.blogspot.com/-tx7bqOIpVbo/TdjCi3cD69I/AAAAAAAAC80/vTUAjErSv0M/s1600/1995%2B28.jpg",
        fanart="http://1.bp.blogspot.com/-tx7bqOIpVbo/TdjCi3cD69I/AAAAAAAAC80/vTUAjErSv0M/s1600/1995%2B28.jpg",
        folder=True )

    # https://i.ytimg.com/vi/O86M_5zYziI/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=6yE545tL5m8cWiWCr6gumw1lEj4
    # http://static.vibe.com/files/2015/08/14165219/stretch-bobbito-radio-that-changed-lives-.png
    plugintools.add_item(
        #action="",
        title="More Freestyles (Stretch Armstrong Show)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://ksr-ugc.imgix.net/projects/2005924/photo-original.jpg?w=640&h=480&fit=crop&v=1439384989&auto=format&q=92&s=da5676819ae4c4033a59928258e60ce8",
        fanart="https://ksr-ugc.imgix.net/projects/2005924/photo-original.jpg?w=640&h=480&fit=crop&v=1439384989&auto=format&q=92&s=da5676819ae4c4033a59928258e60ce8",
        folder=True )

    # https://i.ytimg.com/vi/TtsFwMC6Nmc/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=RZy81Sbeg7B6i1rIg7JoSRWtCQs
    plugintools.add_item(
        #action="",
        title="Stretch Armstrong Show w/ Bobbito and Lord Sear",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://klekt.s3.amazonaws.com/730875.jpg",
        fanart="https://klekt.s3.amazonaws.com/730875.jpg",
        folder=True )
run()
