class Observable:
    
    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        
    def detach(observer):
        self.observers.remove(observer)
        
    def notify_Observers():
        for observer in observers:
            observer.update(self)