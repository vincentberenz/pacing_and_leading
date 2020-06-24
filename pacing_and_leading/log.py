import time,os

FILENAME = "pacing_and_leading.save"

class LogItem:

    __slots__=("time","cursor","soft_target",
               "hard_target","similarity")
    
    def __init__(self,t,cursor,
                 soft_target,hard_target,
                 similarity):
        self.time = t
        self.cursor = cursor
        self.soft_target = soft_target
        self.hard_target = hard_target
        self.similarity = similarity

    def __repr__(self):
        return str([repr(getattr(self,attr))
                    for attr in self.__slots__])


    def __eval__(self,str):
        ar = eval(str)
        for a,attr in zip(ar,self.__slots__):
            setattr(self,attr,a)



class Log:

    def __init__(self):
        self.data = []

    def set(self,cursor,soft_target,
            hard_target,similarity):
        self.data.append(LogItem(time.time(),
                                 cursor,
                                 soft_target,
                                 hard_target,
                                 similarity))


    def save(self,file_path=None):
        if file_path is None:
            file_path = os.getcwd()+os.sep+FILENAME
        with open(file_path,"w+") as f:
            f.write(repr(self.data))
        return file_path
        
    @classmethod
    def load(cls,file_path=None):
        if file_path is None:
            file_path = os.getcwd()+os.sep+FILENAME
        with open(file_path,"r") as f:
            content  = f.read()
        instance = Log()
        instance.data  = eval(content)
        return instance
        
        
