#!/usr/bin/python3

from cmd import Cmd
from models.base_model import BaseModel


class HBNBCommand(Cmd):
    prompt = "(hbnb) "
    class_list = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit in console"""
        print("Exit")
        return True

    def do_create(self, arg):
        if not arg:
            print("** class name mising **")
            return
        classArgs = arg.split()
        className = classArgs[0]
        if className not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            newInst = eval(className)()
            newInst.save()
            print(newInst.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
