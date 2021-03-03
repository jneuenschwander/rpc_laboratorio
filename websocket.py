import asyncio
import websockets, json
from xmlrpc.client import ServerProxy


async def getallnoticias(websocket, path):
    if path == "/getallnoticias":
        await getnoticias(websocket)
    elif path == "/editnoticia":
        await editnoticia(websocket)

    elif path == "/deletenoticia":
        await eliminarnoticia(websocket)
    else:
        await websocket.send("ruta no encontrada")


async def getnoticias(websocket):
    data = []
    for i in rpc.listTile():
        line = i.split(',')
        lineToJson = {
            "id": int(line[0]),
            "titular": line[1],
            "autor": line[4],
            "contenido": line[5],
        }
        data.append(lineToJson)
    print(data)
    msg = json.dumps(data)
    print(msg)
    await websocket.send(msg)


async def editnoticia(websocket):
    jsontext = await websocket.recv()
    peticionjson = json.load(jsontext)
    rpc.edit(peticionjson, 'admin')
    await websocket.send()


async def eliminarnoticia(websocket):
    jsontext = await websocket.recv()
    peticionjson = json.load(jsontext.decode("utf-8"))
    index = peticionjson['ID']
    rpc.delete(index, 'admin', 'True')
    await websocket.send({"estado": "done"})


print('socket en funcionamiento en el puerto 5000')
rpc = ServerProxy('http://localhost:8000', allow_none=True)
start_server = websockets.serve(getallnoticias, "localhost", 5000)
asyncio.get_event_loop().run_until_complete(start_server)  # probar si esto es valido dentro de una instancia
asyncio.get_event_loop().run_forever()
