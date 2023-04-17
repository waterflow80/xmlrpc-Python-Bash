# xmlrpc-Python-Bash
A Python3.x implementation of the XML-RPC protocol

## How it works
- The server.py has a method named `sum`
- The server.py will listen on port 8000 for requests (POST request in our case) that will invoke the method `sum`
- The server uses a library class named SimpleXMLRPCServer from xmlrpc.server module to automate the translation of the 
incoming xml requests
- We can call the remote method `sum` from a Python client (or any other language that implements the xml-rpc library) using the xmlrpc.client
module by specifying the url "http://localhost:8000/", and calling `proxy.sum(arg1,arg2)` after initializing the proxy instance.
- We can also call the method `sum` directly without a high level programming language using `curl` command and sending the body of the **request** in 
xml format that contains the required xml-rpc request tags. An example of the curl command (using Ubuntu) would be :  
   - `$ curl -H "content-type:text/xml" http://127.0.0.1:8000/ --data @reqPy.xml -X POST` 
  
   - reqPy.xml: 
  `<?xml version="1.0"?><methodCall><methodName>sum</methodName><params><param><value><int>6</int></value></param><param><value><int>1</int></value></param></params></methodCall>` calling `sum(6,1)`(Be careful when you use indentations \t while writing the document) 

- The **response** would be something like this:
  `<?xml version='1.0'?><methodResponse><params><param><value><int>7</int></value></param></params></methodResponse>`
