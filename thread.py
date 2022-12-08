# Threads in python are an entity within a process that can be scheduled for execution. In simpler words, a thread is a computation process that is to be performed by a computer. It is a sequence of such instructions within a program that can be executed independently of other codes.
#############################################################################################################
import threading

class thread(threading.Thread):
	def __init__(self, thread_name, thread_ID):
		threading.Thread.__init__(self)
		self.thread_name = thread_name
		self.thread_ID = thread_ID

		
	def run(self):
		print(str(self.thread_name) +" "+ str(self.thread_ID));

thread1 = thread("Test-1", 1000)
thread2 = thread("Test-2", 2000)

thread1.start()
thread2.start()

print("\nExit")
#############################################################################################################
# Now let’s look into what we did up there in the code.  

# We created a sub-class of the thread class.
# Then we override the __init__ function of the thread class.
# Then we override the run method to define the behavior of the thread.
# The start() method starts a Python thread. 
