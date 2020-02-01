import u2py
import os

class UniverseMatrix:

    def __init__(self):
        self.d = {}

    def __getitem__(self,key):
        if not isinstance(key, tuple):
            if key in self.d:
                AM_POS = key - 1
                return self.d[AM_POS]
            else:
                return ''
        else:
            if len(key) == 2:
                AM_POS = key[0] - 1 
                VM_POS = key[1] - 1

                if AM_POS not in self.d:
                    return ''
                if not isinstance(self.d[AM_POS], dict):
                    return ''
                if VM_POS not in self.d[AM_POS]:
                    return ''

                return self.d[AM_POS][VM_POS]

            elif len(key) == 3:
                AM_POS = key[0] - 1 
                VM_POS = key[1] - 1
                SVM_POS = key[2] - 1

                if AM_POS not in self.d:
                    return ''
                if VM_POS not in self.d[AM_POS]:
                    return ''
                if SVM_POS not in self.d[AM_POS][VM_POS]:
                    return ''

                return self.d[AM_POS][VM_POS][SVM_POS]

            elif len(key) == 4:
                AM_POS = key[0] - 1 
                VM_POS = key[1] - 1
                SVM_POS = key[2] - 1
                TM_POS = key[3] - 1

                if AM_POS not in self.d:
                    return ''
                if VM_POS not in self.d[AM_POS]:
                    return ''
                if SVM_POS not in self.d[AM_POS][VM_POS]:
                    return ''
                if TM_POS not in self.d[AM_POS][VM_POS][SVM_POS]:
                    return ''

                return self.d[AM_POS][VM_POS][SVM_POS][TM_POS]

    def __setitem__(self,key,value):
        if not isinstance(key, tuple):
            AM_POS = key - 1 if key != -1 else key
            max_key = max(self.d, key=int) + 1 if self.d else 0 
            AM_POS = max_key if AM_POS == -1 else AM_POS 
            self.d[AM_POS] = value

        else:
            if len(key) == 2:
                AM_POS = key[0] - 1 if key[0] != -1 else key[0] 
                VM_POS = key[1] - 1 if key[1] != -1 else key[1]
                if AM_POS not in self.d:
                    max_key = max(self.d, key=int)+1 if self.d else 0 
                    AM_POS = max_key if AM_POS == -1 else AM_POS 
                    self.d[AM_POS] = {}

                if AM_POS in self.d and not isinstance(self.d[AM_POS], dict):
                    t = self.d[AM_POS]
                    self.d[AM_POS] = {}
                    self.d[AM_POS][0] = t

                if VM_POS == -1:
                    max_key = max(self.d[AM_POS], key=int)+1 if self.d[AM_POS] else 0 
                    VM_POS = max_key 

                self.d[AM_POS][VM_POS] = value

            elif len(key) == 3:
                AM_POS = key[0] - 1 if key[0] != -1 else key[0]
                VM_POS = key[1] - 1 if key[1] != -1 else key[1]
                SVM_POS = key[2] - 1 if key[2] != -1 else key[2]

                if AM_POS not in self.d:
                    max_key = max(self.d, key=int)+1 if self.d else 0 
                    AM_POS = max_key if AM_POS == -1 else AM_POS 
                    self.d[AM_POS] = {}

                if VM_POS not in self.d[AM_POS]:
                    max_key = max(self.d[AM_POS], key=int)+1 if self.d[AM_POS] else 0 
                    VM_POS = max_key if VM_POS == -1 else VM_POS 
                    self.d[AM_POS][VM_POS] = {}

                if VM_POS in self.d[AM_POS] and not isinstance(self.d[AM_POS][VM_POS], dict):
                    t = self.d[AM_POS][VM_POS]
                    self.d[AM_POS][VM_POS] = {}
                    self.d[AM_POS][VM_POS][0] = t 

                if SVM_POS == -1:
                    max_key = max(self.d[AM_POS][VM_POS], key=int)+1 if self.d[AM_POS][VM_POS] else 0 
                    SVM_POS = max_key 

                self.d[AM_POS][VM_POS][SVM_POS] = value

            elif len(key) == 4:
                AM_POS = key[0] - 1 if key[0] != -1 else key[0]
                VM_POS = key[1] - 1 if key[1] != -1 else key[1]
                SVM_POS = key[2] - 1 if key[2] != -1 else key[2]
                TM_POS = key[3] - 1 if key[3] != -1 else key[3]

                if AM_POS not in self.d:
                    max_key = max(self.d, key=int)+1 if self.d else 0 
                    AM_POS = max_key if AM_POS == -1 else AM_POS 
                    self.d[AM_POS] = {}

                if VM_POS not in self.d[AM_POS]:
                    max_key = max(self.d[AM_POS], key=int)+1 if self.d[AM_POS] else 0 
                    VM_POS = max_key if VM_POS == -1 else VM_POS 
                    self.d[AM_POS][VM_POS] = {}

                if SVM_POS not in self.d[AM_POS][VM_POS]:
                    max_key = max(self.d[AM_POS][VM_POS], key=int)+1 if self.d[AM_POS][VM_POS] else 0 
                    SVM_POS = max_key if SVM_POS == -1 else SVM_POS 
                    self.d[AM_POS][VM_POS][SVM_POS] = {}

                if SVM_POS in self.d[AM_POS][VM_POS] and not isinstance(self.d[AM_POS][VM_POS][SVM_POS], dict):
                    t = self.d[AM_POS][VM_POS][SVM_POS]
                    self.d[AM_POS][VM_POS][SVM_POS] = {}
                    self.d[AM_POS][VM_POS][SVM_POS][0] = t 

                if TM_POS == -1:
                    max_key = max(self.d[AM_POS][VM_POS][SVM_POS], key=int)+1 if self.d[AM_POS][VM_POS][SVM_POS] else 0 
                    TM_POS = max_key 

                self.d[AM_POS][VM_POS][SVM_POS][TM_POS] = value


    def u2(self):
        old_cwd = os.getcwd()
        os.chdir("/usr/uv")
        data = u2py.DynArray(self._dict_to_array(self.d))
        os.chdir(old_cwd)
        return data

    def _dict_to_array(self,f):
        dictlist = []
        max_key = max(f, key=int)
        for ctr in range(0,max_key+1):
            key = ctr	
            if key in f:
                value = f[key]
                temp = value
                if isinstance(value,dict):
                    dictlist.append(self._dict_to_array(value))
                else:	
                    dictlist.append(temp)
            else:
                dictlist.append("")

        return dictlist

    def __repr__(self):
        return str(self.d)
