#!/usr/bin/python3

from cmd import Cmd
from models import storage
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

    def do_show(self, arg):
        """
        prints the string representation of an instance based on className and id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] is not HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            key = class_name + "." + args[1]
            allObjs = storage.all()
            if key in allObjs:
                print(allObjs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        pass

    def do_all(self, arg):
        pass

    def do_update(self, arg):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
