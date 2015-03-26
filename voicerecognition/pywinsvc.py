import win32service
import win32serviceutil
import win32api
import win32con
import win32event
import win32evtlogutil
import os, sys, string, time

class aservice(win32serviceutil.ServiceFramework):

    _svc_name_ = "MyServiceShortName"
    _svc_display_name_ = "A python test"
    _svc_description_ = "Writing to a log"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)           

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)                    

    def SvcDoRun(self):
        import servicemanager      
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,servicemanager.PYS_SERVICE_STARTED,(self._svc_name_, '')) 
        self.timeout = 1000     #1 seconds
        # This is how long the service will wait to run / refresh itself (see script below)

        while 1:
            # Wait for service stop signal, if I timeout, loop again
            rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
            # Check to see if self.hWaitStop happened
            if rc == win32event.WAIT_OBJECT_0:
                # Stop signal encountered
                servicemanager.LogInfoMsg("SomeShortNameVersion - STOPPED!")  #For Event Log
                break
            else:
                # What to run
                try:
                  file_path = "D:\Pyprograms\Utilities\src\voicerecognition\tester.py"
                  execfile(file_path)
                except:
                  pass
                #end of what to run


def ctrlHandler(ctrlType):
   return True

if __name__ == '__main__':   
   win32api.SetConsoleCtrlHandler(ctrlHandler, True)   
   win32serviceutil.HandleCommandLine(aservice)