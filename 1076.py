resist_val={"black": 0, 
            "brown": 1, 
            "red": 2, 
            "orange": 3, 
            "yellow": 4, 
            "green": 5, 
            "blue": 6, 
            "violet": 7, 
            "grey": 8, 
            "white": 9
}
resist_mul={"black": 10**0, 
            "brown": 10**1, 
            "red": 10**2, 
            "orange": 10**3, 
            "yellow": 10**4, 
            "green": 10**5, 
            "blue": 10**6, 
            "violet": 10**7, 
            "grey": 10**8, 
            "white": 10**9
}
s=str(resist_val[input()])
s+=str(resist_val[input()])
s=int(s)*resist_mul[input()]
print(s)