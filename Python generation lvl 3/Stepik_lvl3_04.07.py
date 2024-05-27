# import os

# for elem in os.uname():
#     print(elem)

# print(os.ctermid())


# for elem in os.environ:
#     print(elem)

# print(os.getenv("HOME"))

# print(os.getcwd())
# print(os.listdir(os.getcwd())[0])

# print(os.path.getsize(os.getcwd()))

# for elem in os.walk(os.getcwd()):
#     print(elem)
#     print()

# a = os.getcwd()
# print(type(os.path.split(a)))

# print(os.pathconf(os.getuid()))

# my_path = os.getcwd()
# for elem in os.fwalk(my_path):
#     print(elem[4])
#     break

# print(os.times())
# print(help(os.wait))



# import shelve

# # save to shelf
# my_shelf = shelve.open("etc/shelve_example")
# my_shelf["my_list"] = [1, 2, 3, 4, 5]
# my_shelf["my_dict"] = {"a": "apple", "b": "banana", "c": "carrot", "d": "durian", "e": "eggplant"}
# my_shelf.close()

# load from shelf
# with shelve.open("etc/shelve_example") as sh:
#     my_list = sh["my_list"]
#     my_dict = sh["my_dict"]
# print(my_list)
# print(my_dict)

# import shelve
# with shelve.open("etc/shelve_example") as sh:
#     my_list = sh["my_list"]
#     my_list.append(12)
#     sh["my_list"] = my_list

# with shelve.open("etc/shelve_example") as sh:
#     print(sh["my_list"])


# import shelve
# with shelve.open("etc/shelve_example", writeback=True) as sh:
#     my_list = sh["my_list"]
#     my_list.append(15)
#     sh.sync()

# with shelve.open("etc/shelve_example") as sh:
#     print(sh["my_list"])


# import shelve
# with shelve.open("etc/shelve_example") as sh:
#     for k, v in sh.items():
#         print(k, v)


# import dbm
# with dbm.open("etc/dbm_object", "c") as db:
#     db["name"] = b"Piter"
#     db["age"] = b"30"


# with dbm.open("etc/dbm_object", "r") as db:
#     for elem in db.keys():
#         print(elem, db[elem])


