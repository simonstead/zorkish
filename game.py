import cmd, sys, textwrap

test_string = "You are standing in an open field west of a white house, with a boarded front door. There is a small mailbox here."

SCREEN_WIDTH = 80


def wrap(text):
    for line in textwrap.wrap(test_string, SCREEN_WIDTH):
        print(line)


def move(direction):
    print "You moved %s" % direction


def describe_room():
    print("You're in a room")


def describe_object(thing):
    print(thing)


class GameCommands(cmd.Cmd):
    prompt = "\n> "

    def default(self, arg):
        print(
            'I do not understand that command. Type "help" for a list of commands.'
        )

    def do_quit(self, arg):
        """Quit the game."""
        return True  # this exits the Cmd application loop in TextAdventureCmd.cmdloop()

    # to lower case probably
    # a move function (current_room is x,y coord on grid)
    def do_go(self, direction):
        """Move in a direction. Valid inputs are \n- north\n- east\n- south\n- west"""
        if direction in ["north", "east", "south", "west"]:
            move(direction)
        else:
            print("\nEnter north, east, south or west to move in a direction")

    def do_look(self, thing):
        """'look' to look around the room, or 'look [at|in] {thing}' to describe the thing"""
        if thing == "":
            describe_room()
        else:
            if thing[:3] == "at " or thing[:3] == "in ":
                thing = thing[3:]
            describe_object(thing)


if __name__ == '__main__':
    print("\n\nOMG IT'S A TEXT ADVENTURE GAME\n\nPRESS help FOR HELP\n\n")
    wrap(test_string)
    GameCommands().cmdloop()
    print('\nYou escaped without being eaten by a grue\n')
