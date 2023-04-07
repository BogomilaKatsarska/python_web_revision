'''
1. Internet - vast network that connects billions of devices together all over the world:
- ISP - Internet Service Provider
- Network - a group of two or more devices that can communicate
- Web Client(our browser - Internet Explorer, Mozilla, FireFox..) sends Request to Web Server.
  Web Server receives the Request and sends it to Technology (Our Application).
  Technology connects to DB and returns requested resources.
- Servers are the machines that provide services to other machines
- Clients are the machines that are used to connect to those services
- Network Protocol - set of rules and standards that allow communication between network devices
- Packets - every message, file or stream of information sent over computer networks is broken
  down into small chunks called packets. Contents/Origin/Destination
- IP address (Internet Protocol Address)- All the devices on the Internet have IP Address. Each IP address is unique to each computer or
  a device at the edge of the network
- DNS - The domain name is a human way to access IP address for devices and websites around the world (example: softuni.bg)

2. HTTP (Hyper Text Transfer Protocol):
- Methods/CRUD/:
POST - create / store a resource
GET - read / retrieve a resource
PUT - update / modify a resource (also PATCH)
DELETE - delete / remove a resource
HEAD - returns the meta data
OPTIONS - checks the client's access to the mentioned resource

3. URL - Uniform Resource Locator:
HTTP - port:80
HTTPS - port:443

protocol - host - port - path - query string - fragment

4. Dev Tools:
- Mozilla Dev Tools
- Postman
- Rested
- curl - can be automated

5. MIME/Multi-Purpose Internet Mail Extensions/ and Media Types:
- standard for encoding resources
- == content type
- body == payload
#TODO: CHECK IF: PRESERVE LOGS == PERSIST LOGS
#TODO: CHECK POSTMAN, CURL

6. HTTP Response Codes:
- 1xx: Informational (100 - Continue)
- 2xx: Successful (200 - OK, 201 - Created)
- 3xx: Redirection (304 - Not Modified, 301 - Moved Permanently, 302 - Found)
- 4xx: Client error (400 - Bad request, 404 - Not found, 401 - Unauthorized, 409 - Conflict)
- 5xx: Server error (500 - Internal server error, 503 - Service unavailable)
'''