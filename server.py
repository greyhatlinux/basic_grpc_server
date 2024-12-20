import grpc
from concurrent import futures
import mysql.connector
import message_pb2 as pb2
import message_pb2_grpc as pb2_grpc
from grpc_reflection.v1alpha import reflection


class EmployeeService() :
    def GetEmployee(self, request, context):
        id = request.id
        try:            
            print("Connecting to DB!")
            connection = mysql.connector.connect(
                host='127.0.0.1',
                port=8101,
                user='root',
                password='pass',
                database='users_db',
            )
            cursor = connection.cursor()
            cursor.execute(f'SELECT * from users WHERE id={id}')
            response = cursor.fetchone()
            print(response)
            id, name, email = response[0], response[1], response[2]
            return pb2.Response(name=name, email=email)
        except Exception as e:
            print("Couldn't fetch records!")
            print(e)

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_EmployeeServicer_to_server(EmployeeService(), server)
    
    # Add server reflection 
    SERVICE_NAMES = (
        pb2.DESCRIPTOR.services_by_name['Employee'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    
    server.add_insecure_port('[::]:9999')

    try :
        server.start()
        print("Server running on port 9999")
        server.wait_for_termination()
    except any as e:
        print("Sever couldn't start")
        print(e)
    
if __name__ == '__main__':
    server()
    

    