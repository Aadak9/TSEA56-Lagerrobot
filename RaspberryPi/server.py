import asyncio
 
PORT = 12345
HOST = "0.0.0.0"
 
async def handle_client(reader, writer):
	addr.writer.get_extra_info('peername')
	print(f"Ny anslutning från {addr}")
	
	async def recieve_data(): 
		while True:
			data = await reader.read(100)
			if not data:
				print("Klient kopplade från")
				break
			message = data.decode()
			print(f"Mottaget från {addr}: {message}")
			
	async def send_data():
		while True:
			message = input("Skriv meddelande att skicka: ")
			writer.write(message.encode())
			await writer.drain()
	
	await asyncio.gather(recieve_data(), send_data())

	 
async def main():
	server = await asyncio.start_server(handle_client, HOST, PORT,
		reuse_address = True, reuse_port = True)
	print(f"Server startad på {HOST}:{PORT}")
	
	async with server:
		print("Hej")
		await server.serve_forever()
	
	print("då")
	
asyncio.run(main())


	
