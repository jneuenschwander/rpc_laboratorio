from xmlrpc.server import SimpleXMLRPCServer


class RPC:
    _metodo_rpc = ['signin', 'login', 'post', 'edit', 'delete', 'listTile', 'searchUser']

    def __init__(self, direccion):
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)
        for metodo in self._metodo_rpc:
            self._servidor.register_function(getattr(self, metodo))
    def signin(self, data):
        a = self.searchUser(data)
        if(a == None):
            self.insertUser(data)
            return True
        else:
            return False
    def login(self, data):
        datos = data.split(',')
        rta = self.searchUser(data).split(',')
        if datos[0] == rta[0] and datos[1] == rta[1]: #usuario  y clave
            return True
        else:
            return False
    def post(self,data, usuario):
        with open("post.txt", "r") as file:
            for last_line in file:
                pass
        index = int(last_line.split(',')[0])+1
        file.close()
        f = open('post.txt', 'a')
        f.write('\n'+str(index)+','+usuario+','+data)
        f.close()
    def edit(self,index,user,edit):
        self.editpost(index,user, edit) # error
    def delete(self, index, user,op):
        with open("post.txt", "r+") as f:
            lines = f.readlines()
            if lines[index-1].split(',')[1]==user or op == 'True':
                del lines[index-1]
                f.seek(0)
                f.truncate()
                f.writelines(lines)
                return True
            else:
                return False
    def listTile(self):
        with open('post.txt','r') as f:
            ans = f.readlines()
            return ans
    def editpost(self, index, user ,edit):
        with open('post.txt','r') as f:
            data = f.readlines()
            if len(data) == 0:
                return False
            elif len(data) == 1:

                dataIndex = data[0].split(',')[0]
                dataUser = data[0].split(',')[1]
                if int(dataIndex) == index and dataUser == user: #corregir
                    data[0] = data[0].replace(data[0].split(',')[2],edit.split(',')[0]) # remplazo titulo
                    data[0] = data[0].replace(data[0].split(',')[3], str(edit.split(',')[1]+'\n')) # remplazo contenido
                    with open('post.txt', 'w') as file:
                        file.writelines(data)
                        return True
            elif len(data ) > 1:
                for i in range(len(data)): # recorro todas las lineas
                    dataIndex = data[i].split(',')[0]
                    dataUser = data[i].split(',')[1]
                    if int(dataIndex) == index and dataUser  == user:
                        data[i] = data[i].replace(data[i].split(',')[2], edit.split(',')[0])  # remplazo titulo
                        data[i] = data[i].replace(data[i].split(',')[3],
                                                  str(edit.split(',')[1] + '\n'))  # remplazo contenido
                        with open('post.txt', 'w') as file:
                            file.writelines(data)
                            return True
        return False
    def searchUser(self, data):
        with open('usuarios.txt','r') as f:
            for line in f:
                if data in line:
                    return line
    def insertUser(self, data):
        f= open('usuarios.txt','a')
        f.write('\n'+data+',False')
        return True
    def iniciar_servidor(self):
        self._servidor.serve_forever()
if __name__ == '__main__':

    rpc = RPC(('', 8000))
    print('Se establecio la conexión')
    rpc.iniciar_servidor()