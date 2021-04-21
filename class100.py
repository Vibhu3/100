class Car(object):
    def __init__(self,modal,color,company,speed_limit):
        self.color=color 
        self.company=company
        self.modal=modal
        self.speed_limit=speed_limit
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerating")
audi=Car("a6","red","audi","80")
print( audi.start())
print( audi.stop())
print( audi.accelerate())
toyota=Car("a7","blue","toyota","90")
toyota.start()
toyota.stop()
toyota.accelerate()