#Q.3.

class Customer:
    def validate_quantity(self, qty):
        if (qty>=1 and qty<=5):
            return True
        else:
            return False
class PizzaService:
    c=100
    def __init__(self, ptype,qty,topping):
        self.ptype=ptype
        self.qty=qty
        self.topping=topping
        self.pcost=-1
        
    def validate_ptype(self):
        if self.ptype.lower()=="small" or self.ptype.lower()=="medium":
            return True
        else:
            return False
    
    def cal_cost(self):
        if self.validate_ptype() and Customer().validate_quantity(self.qty):
            pizza_cost_table = {"small":150,"medium":200}
            cost = {"small":35,"medium":50}
            
            pcost = pizza_cost_table[self.ptype.lower()] * self.qty
            if self.topping:
                pcost += cost[self.ptype.lower()] * self.qty
                
            self.pcost = pcost
            self.s_id = self.ptype[0]+str(PizzaService.c+1)
            PizzaService.c += 1
            
        else:
            self.pizza_cost = -1
    
class DoorDelivery(PizzaService):
    def __init__(self, ptype,qty,topping,distance):
        super().__init__(ptype, qty,topping)
        self.distance=distance
        
    def validate_dis(self):
        if self.distance>=1 and self.distance<=10:
            return True
        else:
            return False
        
    def cal_cost(self):
        if self.validate_dis() and super().cal_cost() != -1:
            if self.distance<=5:
                self.pcost+=5*self.distance
            else:
                self.pcost+=5*self.qty
                self.pcost+=7*(self.distance-5)*self.qty           
        else:
            self.pcost=-1



pizza_service=PizzaService("Small",3,True)
pizza_service.cal_cost()
print("Service ID:",pizza_service.s_id)
print("Pizza cost:",pizza_service.pcost)

door_delivery=DoorDelivery("Medium",2,False,8)
door_delivery.cal_cost()
print("Service ID:",door_delivery.s_id)
print("Pizza cost:",door_delivery.pcost)




            
        






