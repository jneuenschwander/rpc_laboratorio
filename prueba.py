import asyncio
import websockets


async def getallnoticias(websocket, path):
    if path == "/getallnoticias":
        await getnoticias(websocket)
    elif path == "/editnoticia":
        name = await websocket.recv()
        print(f"< {name}")

        greeting = f"Edit {name}!"

        await websocket.send(greeting)
        print(f"> {greeting}")

    elif path == "/deletenoticia":
        name = await websocket.recv()
        print(f"< {name}")

        greeting = f"Delete {name}!"

        await websocket.send(greeting)
        print(f"> {greeting}")
    else:
        await websocket.send("ruta no encontrada")


async def getnoticias(websocket):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Get {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")


start_server = websockets.serve(getallnoticias, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
