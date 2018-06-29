def demystify (l1_string):
        first_replacement=l1_string.replace("l", "a")
        return first_replacement.replace("1", "b")
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
