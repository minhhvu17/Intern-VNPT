class Producer:
    def __init__(self, pId):
        self.id = pId
    def sendMessage(self):
        message = input("Enter message: ")
        format_message = f"Message from Producer ({self.id}): {message}"
        return format_message

class Customer:
    def __init__(self, cId):
        self.id = cId
        self.receivedMessage = []
    def getMessageReceived(self):
        for idx, message in enumerate(self.receivedMessage):
            print(f"Index {idx} - Message: {message}")

class Queue:
    def __init__(self):
        self.queue = []
    def receive(self, message):
        self.queue.append(message)
        print("Message recieved!")
    def getMessageReceived(self):
        for idx, message in enumerate(self.queue):
            print(f"Index {idx} - Message: {message}")
    def send(self, customer):
        customer.receivedMessage.append(self.queue[0])
        self.queue.pop(0)
        print("Message sent!")
        
def main():
    queue = Queue()
    producerList = [Producer(0), Producer(1), Producer(2)]
    customerList = [Customer(0), Customer(1)]
    while True:
        print("1 -- Receive message        2 -- Display Queue       3 -- Send message       4 -- Exit")
        option = int(input("Option: "))
        if option == 1:
            try:
                producerId = int(input("Message sent from producer ID: "))
                queue.receive(producerList[producerId].sendMessage())
            except IndexError:
                print("Producer not exist")
        elif option == 2:
            queue.getMessageReceived()
        elif option == 3:
            try:
                customerId = int(input("Send message to customer ID: "))
            except IndexError:
                print("Customer not exist")
            try:    
                queue.send(customerList[customerId])
            except IndexError:
                print("No message in queue")
            
        elif option == 4:
            break
        else:
            print("Wrong syntax!")
            
    
if __name__ == "__main__":
    main()
