from component.appflask import app
import core.app
import threading
#from warning import main_warning

class FlaskServer(threading.Thread):
    def run(self) -> None:
        core.app
        app.run(host='localhost',port=5000)


#class warning(threading.Thread):
#    def run(self) -> None:
#        main_warning

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    flaskthread = FlaskServer()
    flaskthread.start()

    #warningthread = warning()
    #warningthread.start