
# Write your solution here:

class Task:
    id_counter = 0 # class-level variable, keeps track of how many Task classes are created 

    def __init__(self, description: str = "", programmer: str = "", workload: int = 0) -> None:
        self.description = description
        self.programmer = programmer
        self.workload = workload
        
        # default status is False / NOT FINISHED 
        self.finished = False
        
        Task.id_counter += 1
        # class variable 
        self.id = Task.id_counter

    def is_finished(self):
        return self.finished
            
    def mark_finished(self):
        self.finished = True
    
    def __str__(self):
            status = "FINISHED" if self.finished else "NOT FINISHED"
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self) -> None:
        self._all_orders = []


    def add_order(self, description, programmer, workload):

        task_obj = Task(description, programmer, workload)
        self._all_orders.append(task_obj)

    def all_orders(self):
        return self._all_orders
    
    # creates a set, which is converted to a list 
    def programmers(self):
        return list(set(order.programmer for order in self._all_orders))

    # takes id of matching Task obj and marks relevant task as finished 
    def mark_finished(self, id: int):
        for order in self._all_orders:
            if order.id == id: # unsure about order.id because Task.id is class variable? 
                order.mark_finished() # Task obj method ``
                return 
        raise ValueError("NO ID MATCHED FOR TASK")
    
    def finished_orders(self):
        return [order for order in self._all_orders if order.is_finished()] 
    
    def unfinished_orders(self):
        return [order for order in self._all_orders if not order.is_finished()] 

    
    def status_of_programmer(self, programmer: str) -> tuple:
        if any(order.programmer == programmer for order in self._all_orders): 
            task_done = sum([1 for order in self._all_orders if order.programmer == programmer and order.is_finished() == True])
            task_undone = sum([1 for order in self._all_orders if order.programmer == programmer and order.is_finished() == False])

            num_done_hours = sum([order.workload for order in self._all_orders if order.programmer == programmer and order.is_finished()])
            num_undone_hours = sum([order.workload for order in self._all_orders if order.programmer == programmer and not order.is_finished()])
    
            return task_done, task_undone, num_done_hours, num_undone_hours
        
        raise ValueError("STATUS OF PROGRAMMER ERROR")
