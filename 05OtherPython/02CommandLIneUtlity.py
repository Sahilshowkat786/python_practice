import argparse
parse=argparse.Argunmentparse()
parse.add_argunment("name")
arg=parse.parse_args()
print(f"Hello, {arg.name}")
