# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2018 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from .handler import Handler


class DeletedMessagesHandler(Handler):
    """The Deleted Message handler class. Used to handle deleted messages coming from any chat
    (private, group, channel). It is intended to be used with
    :meth:`add_handler() <pyrogram.Client.add_handler>`

    Args:
        callback (``callable``):
            Pass a function that will be called when a new Message arrives. It takes *(client, message)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters <pyrogram.Filters>`):
            Pass one or more filters to allow only a subset of messages to be passed
            in your callback function.

    Other parameters:
        client (:obj:`Client <pyrogram.Client>`):
            The Client itself, useful when you want to call other API methods inside the message handler.

        message (:obj:`Message <pyrogram.Message>`):
            The received message.
    """

    def __init__(self, callback: callable, filters=None):
        super().__init__(callback, filters)

    def check(self, messages):
        return (
            self.filters(messages.messages[0])
            if self.filters
            else True
        )
