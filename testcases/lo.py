class koo:
    def __int__(self):
        self.ok="fjk"
    def __setattr__(self, key, value):
        print("dskjfd")
        super.__setattr__(self,key,value)

hu=koo()
print(hu.ok)