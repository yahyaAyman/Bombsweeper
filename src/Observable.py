class Observable:
    observers = []
    def __init__(self):
        self.observers = observers
    def attach(self, observer):
        self.observers.append(observer)
        
    def detach(self, observer):
        self.observers.remove(observer)
        
    def notify_Observers(self, grid):
        for observer in self.observers:
            observer.update(grid)
