import grpc
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'proto')))
import calculator_pb2 as calculator_pb2
import calculator_pb2_grpc as calculator_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    
    while True:
        user_input = input("Input (or -1 to exit): ") # e.g., "add 1 2"
        if user_input == "-1":
            break
        
        try:
            operation, num1_str, num2_str = user_input.split()
            num1, num2 = int(num1_str), int(num2_str)
            
            response = stub.Calcul(calculator_pb2.Request(cal=operation, num1=num1, num2=num2))
            ansr = response.result.replace('"', '')
            print(f"Result: {ansr}")
        except ValueError:
            print("Invalid input. Please use the format 'add num1 num2'.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    channel.close()
        
if __name__ == '__main__':
    run()
