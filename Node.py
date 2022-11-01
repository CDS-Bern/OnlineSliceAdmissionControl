class Node(object):
    def __init__(self, cpu, ram, storage):
        self.admit_cost = None                
        self.cpu = cpu        
        self.ram = ram      
        self.storage = storage                  

    def CPU(self) -> int:        
        CPU = self.cpu  
        return CPU

    def RAM(self) -> int:
        RAM = self.ram  
        return RAM

    def Storage(self) -> int:
        Storage = self.storage  
        return Storage

    # def BW(self) -> int:
    #     BW = 10  
    #     return BW

    # def online_reservation_function(self):
    #     var = self.admit_cost


