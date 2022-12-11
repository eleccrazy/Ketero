#!/usr/bin/python3
""" console for managing models, It is used only for development purpose"""

import cmd
import models
from models.user import User
from models.base import BaseModel
from models.city import City
from models.hospital import Hospital
from models.service import Service
import shlex


class CustomException(Exception):
    """Custom exception for terminating the consle"""
    pass


classes = {"User": User, "BaseModel": BaseModel, "City": City,
           "Hospital": Hospital, "Service": Service}


class HBNBCommand(cmd.Cmd):
    """ Ketero console """
    prompt = '(ketero) '

    def do_EOF(self, arg):
        """Exits console"""
        print("")
        raise CustomException

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        raise CustomException

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class
        Caution: Don't forget to pass the required parameters while
                 creating instances. (i.e, nullable=False params)
        Usage: create <class name> <required attributes>
        Examples: create City name='Adama'
               create User first_name="Elec" last_name="Crazy" phone="09xxx"
                           email="eleccrazy24@gamil.com" password="ketero"
        Note: If you want to pass two words as a value for the keys, you need
        have to separate them with underscores:
            Example: create City name="Addis_Ababa"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id
        Usage <class name> <instance id>
        Example: show User 53a326ef-47b5-4902-9b04-7548c6589d64
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id
        Usage: destroy <class name> <instance id>
        Example: destroy User 53a326ef-47b5-4902-9b04-7548c6589d64
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances
        I) Usage: all  => This prints all objects stored in the database
            Example: all
        II) Usage: all <class name>  => This prints all objects of a specific
                   Class
            Example: all Hospital
        """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """Updates an instance based on the class name, id, attribute & value
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Example: update User 507d2005-a229-41db-953d-3944d187a709 first_name
                 "King"

        """
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except CustomException:
        print("Thanks for using this console :) Bye!")
