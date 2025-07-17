numOfReq = int(input("Enter number of reuqests: "))

req = []

print("Enter the requests: ")
for _ in range(numOfReq):
    req.append(int(input()))

server1 = []
server2 = []

for i in range(len(req)):
    if i % 2 == 0:
        server1.append(req[i])
    else:
        server2.append(req[i])

print(server1)
print("Requests in server-one are", len(server1))