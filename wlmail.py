#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with Dragonfly.  If not, see
#   <http://www.gnu.org/licenses/>.
#

"""
    This module is a simple shortcuts of Dragonfly use.

    It shows how to use Dragonfly's Grammar, AppContext, and MappingRule
    classes.  This module can be activated in the same way as other
    Natlink macros by placing it in the "My Documents\Natlink folder" or
    "Program Files\NetLink/MacroSystem".

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation,
                       Key, Text)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

grammar_context = AppContext(executable="wlmail")
grammar = Grammar("wlmail_shortcuts", context=grammar_context)


#---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this shortcuts
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

shortcuts_rule = MappingRule(
    name="shortcuts",    # The name of the rule.
    mapping={          # The mapping dict: spec -> action.
                # Windows live mail shortcuts
                "move to folder": Key("cs-v"),
                "sort with date": Key("a-v, b/10, down:1, enter"),
                "sort with flag": Key("a-v, b/11, down:6, enter"),
                'flag': Key("a-a, a"),
                'send to junk': Key("ca-j"),
                #"sort with flag": Key("a-v/200, b/200"), #, right, down/300, enter"), # + 6*"down/20, "), # + "enter"),
                #"sort with from": Key("a-v/200, b/200"), #, right, down/300, enter"), # + 6*"down/20, "), # + "enter"),

                # todo: fix
#                'live emails': ('{esc}{tab}',0x100),
#                # Google wlmail commands
#                'next': Key("c-tab"),
#                'previous': Key("cs-tab"),
#                'private': Key("a-e, i/20"),
#                'close': Key('c-w'),
#                'bookmark': Key('c-d/20'),
#                'tools': Key('a-e'),
#             "save [file]":            Key("c-s"),
#             "save [file] as":         Key("a-f, a"),
#             "save [file] as <text>":  Key("a-f, a/20") + Text("%(text)s"),
#             "find <text>":            Key("c-f/20") + Text("%(text)s\n"),
            },
    extras=[           # Special elements in the specs of the mapping.
            Dictation("text"),
           ],
    )

# Add the action rule to the grammarecurjinstance.
grammar.add_rule(shortcuts_rule)


#---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.

grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
