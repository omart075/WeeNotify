# Requires `brew install terminal-notifier`

import os
import datetime
import weechat

# Information and function call to register script with Weechat (required)
SCRIPT_NAME = 'WeeNotify'
SCRIPT_AUTHOR = 'Oscar Martinez <omart0725@gmail.com>'
SCRIPT_VERSION = '1.0'
SCRIPT_LICENSE = 'GPL'
SCRIPT_DESC = 'Get notifications from Weechat as a Mac Notification'
weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, '', '')


# The notification function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# Function that gets messages on all buffers (sorted out by given restrictions on time and tags)
def get_message(data, buffer, date, tags, is_displayed, is_highlight, prefix, message):

    # needed in case where sender name has space in front (when not an operator of buffer)
    nameToCheck = prefix

    # Time the message was sent
    message_time = datetime.datetime.utcfromtimestamp(int(date))

    # Current time
    now_time = datetime.datetime.utcnow()

    # if message came from core buffer (not a chat)
    if (weechat.buffer_get_string(buffer, 'short_name') == "matrix"):
        return weechat.WEECHAT_RC_OK
    if (weechat.buffer_get_string(buffer, 'short_name') == "weechat"):
        return weechat.WEECHAT_RC_OK

    # if change is made to chat such as topic or name
    if (prefix == "--"):
        return weechat.WEECHAT_RC_OK

    # Checking if message came from yourself from device or terminal
    # Handles space issue
    if (prefix.startswith(" ")):
        nameToCheck = prefix[1:]
    if (weechat.buffer_get_string(buffer, 'localvar_nick') == nameToCheck):
            return weechat.WEECHAT_RC_OK

    # if message is older than 5 seconds (otherwise notifier displays all buffer messages each time)
    if (now_time - message_time).seconds > 5:
        return weechat.WEECHAT_RC_OK

    # Send notification with sender name, buffer name, and message
    notify(title    = prefix,
           subtitle = weechat.buffer_get_string(buffer, 'short_name'),
           message  = message)

    return weechat.WEECHAT_RC_OK

# Call to the get_message function; needs to be hooked for weechat to call it
weechat.hook_print('', '', '', 1, 'get_message', '')
