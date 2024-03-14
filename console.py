#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Place", "Review", "State", "City", "Amenity"]

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
        elif args[0] not in HBNBCommand.class_list:
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
        """
        prints the string representation of an instance based on className and id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            className = args[0]
            key = className + "." + args[1]
            allObjs = storage.all()
            if key in allObjs:
                del allObjs[key]
                storage.save()
            else:
                print("** No instance found **")

    def do_all(self, arg):
        args = arg.split()
        objDict = storage.all()

        if not args:
            new_list = []
            for key, value in objDict.items():
                new_list.append(str(value))
            print(new_list)
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            new_list = []
            for key, value in objDict.items():
                if key.startswitch(args[0] + "."):
                    new_list.append(str(value))
            print(new_list)

    def do_update(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            allObjs = storage.all()
            key = args[0] + "." + args[1]
            if key not in allObjs:
                print("** no instance found **")
            else:
                instance = allObjs[key]
                if instance.__class__.__name__ in HBNBCommand.class_list:
                    setattr(instance, args[2], args[3])
                    instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
