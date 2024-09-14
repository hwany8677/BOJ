#이새끼들 얼불춤하나?
tabeop={
    "fdsajkl;": "in-out",
    "jkl;fdsa": "in-out",
    "asdf;lkj": "out-in",
    ";lkjasdf": "out-in",
    "asdfjkl;": "stairs",
    ";lkjfdsa": "reverse"
}
s=input()
try: print(tabeop[s])
except KeyError: print("molu")