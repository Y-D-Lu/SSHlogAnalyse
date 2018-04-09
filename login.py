import pandas as pd

path = "auth_ex.log"


def file2df():
    f = open(path)  # read from version list

    lines = f.readlines()
    a=0
    name=[]
    pwd=[]
    for auth in lines:
        au = auth.split('sshlog: ')[1]
        # well... something stupid occurred: some attempts of login even do not entered a username. Confused...
        # and some just entered the empty password. Oh, well, assume that a friend of mine never set a password,
        # no matter what device he uses and what occasion he's in. And now, the grass on his tomb has been meters high
        # just be joking XD
        if au.split().__len__()==2:
            name.append(au.split()[0])
            pwd.append(au.split()[1])
    f.close()
    df = pd.DataFrame({"name":name,"pwd":pwd})
    return df


def name_sort(num=10):
    df = file2df()
    return df.groupby("name").size().sort_values(ascending=False).head(num)


def pwd_sort(num=10):
    df = file2df()
    return df.groupby("pwd").size().sort_values(ascending=False).head(num)
