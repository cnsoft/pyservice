import pyservice

class SimpleProcess1(pyservice.Process):
    pidfile = ''
    
    def run(self):
        print 'SimpleProcess1.run()'

class SimpleProcess2(pyservice.Process):
    pidfile = ''

    def run(self):
        print 'SimpleProcess2.run()'


