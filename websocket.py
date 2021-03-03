import asyncio
import websockets, json
from xmlrpc.client import ServerProxy
async def getallnoticias(self, websocket, path):
    if path == "/getallnoticias":
        await self.getnoticias(websocket)
    elif path == "/editnoticia":
        await self.editnoticia(websocket)

    elif path == "/deletenoticia":
        await self.eliminarnoticia(websocket)
    else:
        await websocket.send("ruta no encontrada")


async def getnoticias( websocket):
    data = []
    for i in rpc.listTile():
        line = i.split(',')
        lineToJson = {
            "ID": i[0],
            "Titular": i[1],
            "fechacreacion": i[2],
            "fechaactualizacion": i[3],
            "Autor": i[4],
            "Contenido": i[5],
        }
        data.append(lineToJson)
    msg = json.dumps(data)
    await websocket.send(msg)


async def editnoticia( websocket):
    jsontext = await websocket.recv()
    peticionjson = json.load(jsontext)
    rpc.edit(peticionjson,'admin')
    await websocket.send()



async def eliminarnoticia( websocket):
    jsontext = await websocket.recv()
    peticionjson = json.load(jsontext.decode("utf-8"))
    index = peticionjson['ID']
    rpc.delete(index,'admin','True')
    await websocket.send({"estado":"done"})


print('socket en funcionamiento en el puerto 5000')
rpc = ServerProxy('http://localhost:8000', allow_none= True)
start_server = websockets.serve(getallnoticias, "localhost", 5000)
asyncio.get_event_loop().run_until_complete(start_server)  # probar si esto es valido dentro de una instancia
asyncio.get_event_loop().run_forever()