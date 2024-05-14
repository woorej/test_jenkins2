from concurrent import futures
import grpc
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'proto')))

import calculator_pb2 as calculator_pb2
import calculator_pb2_grpc as calculator_pb2_grpc

class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def __init__(self) -> None:
        pass
    
    def Calcul(self, request, context):
        
        result = calculator_pb2.Response()
        if request.cal == 'add':
            print(f"requested: {request.num1} {request.num2}")
            ansr = self.add(request.num1, request.num2)
            result.result = f"{request.num1} + {request.num2} = {ansr}"
        elif request.cal == 'sub':
            print(f"requested: {request.num1} {request.num2}")
            ansr = self.subtract(request.num1, request.num2)
            result.result = f"{request.num1} - {request.num2} = {ansr}"
        else:
            result.result = "Not supported operation"
        
        return result
        
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    print("Server Start!")
    server.start()
    server.wait_for_termination()

def main():
    serve()
    
if __name__ == '__main__':
    main()
    