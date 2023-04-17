from xmlrpc.server import SimpleXMLRPCServer

def sum(a,b):
    return a + b

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(sum, "sum")
server.serve_forever()