class Animate:
    frame = 0
    order_i = 0
    def __init__(self,f_names, order):
        self.f_names = f_names
        self.order = order

    def update(self):
        #returns sprite string from f_names
        ret_frame = self.order[self.order_i][1]
        
        self.frame += 1
        if self.frame > self.order[self.order_i][0]:
            self.frame = 0
            self.order_i += 1
            if self.order_i > len(self.order) - 1:
                self.order_i = 0

        return self.f_names[ret_frame]
    
    def set_f_names(self,f_names):
        self.f_names = f_names
        self.order_i = 0
        self.frame = 0

    def set_order(self,order):
        self.order = order
        self.order_i = 0
        self.frame = 0