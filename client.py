import grpc 
import mysql.connector
import message_pb2 as pb2
import message_pb2_grpc as pb2_grpc

def connect_and_query(user_id: int):
    with grpc.insecure_channel('localhost:9999') as channel:
        stub = pb2_grpc.EmployeeStub(channel)
        try:
            request = pb2.Request(id=user_id)
            response = stub.GetEmployee(request)
            print(f'{response.name} | {response.email}')
        except grpc.RpcError as e:
            print(f"Couldn't get user with id : {user_id}")
        
if __name__ == '__main__':
    while True:    
        id = int(input("Enter the id : "))
        connect_and_query(id)
        print("---------")






