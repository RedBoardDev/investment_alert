import json
import orjson

class utils_file:
    def load_file(self, path:str):
            with open(path, 'r') as file:
                # try:
                self.file = orjson.loads(file.read())
                # except FileNotFoundError as e:
                #     print (e)


    def f_write(self, path, str): # a voir pour faire argument infini pour le path pour pouvoir faire genre ['balance']['test']
        self.file[path] = str
        with open('data.json', 'w') as file:
            json.dump(self.file, file, indent = 4)

    def f_read(self, path): # a voir pour faire argument infini pour le path pour pouvoir faire genre ['balance']['test']
        try:
            data = self.file[path]
        except KeyError as e:
            raise
        # except FileNotFoundError as e:
        #     return (2)
        return(data)
