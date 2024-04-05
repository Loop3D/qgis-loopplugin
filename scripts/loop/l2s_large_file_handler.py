# This module is to download data from loop3d server
# and save it into the loopstructural_output_data
import asyncio
import websockets

async def receive_file(websocket, file_path):
    """
    websocket       : web link to retrieve packet
    file_path       : the file path to save the data
    """

    try:
        with open(file_path, 'wb') as file:
            async for chunk in websocket:
                file.write(chunk)  # Write the received chunk to the file
    except Exception as e:
        print(f"Error occurred while receiving file: {e}")

async def main():
    #websocket_server = await websockets.serve(receive_file, "localhost", 8765)
    websocket_server = await websockets.serve(receive_file, "10.131.253.163", 8888)
    print("WebSocket server started...")
    await websocket_server.wait_closed()

asyncio.run(main())
