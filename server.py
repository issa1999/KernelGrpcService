# IMPORTING MODULES
import grpc 
import os
import kmodule 
import kmodpy
from concurrent import futures
import Getter.KernelGetterService_pb2 as Getter_pb2
import Getter.KernelGetterService_pb2_grpc as grpc_Getter_pb2
import Setter.KernelSetterService_pb2 as Setter_pb2 
import Setter.KernelSetterService_pb2_grpc as grpc_Setter_pb2 


# To use uname and Kmod 
km = kmodpy.Kmod()
uname = os.uname() 





################################################################
#################    GETTER SERVICE    #########################
################################################################


class GetterService(grpc_Getter_pb2.GETTER_INFORMATIONServicer):

 ############################################################
 #                                                          #
 # Uname command                                            #
 #  -1                                                      #
 ############################################################

  def UNAME(self, request, context):
    print(request) 
    resultat = Getter_pb2.MODULE() 
    resultat.data = "Sysname =  "+ uname.sysname+" | Nodename =  "+ uname.nodename+" | release =  "+ uname.release+" | version =  "+ uname.version+" | Machine =  "+ uname.machine+" | "
    return resultat
 ############################################################
 #                                                          #
 # Uname Modinfo(module)                                    #
 #  -2                                                      #
 ############################################################
  def MODINFO(self, request, context):
    info_list= list(km.modinfo(str(request.data))) # execute the modinfo command on the module given by the client
    for info in info_list: # iterate over each information
      resultat = Getter_pb2.MODULE() # create the return values 
      resultat.data = str(info[0])[1::] + " = " + str(info[1])[1::] + "\n" # format the return values and add the to the response 
      yield resultat # return the informationns
 ############################################################
 #                                                          #
 # Lsmod  command                                           #
 #   -3                                                     #
 ############################################################
  def ALL_MODULES(self, request, context): # Displaying all kernel modules
    resultat=Getter_pb2.MODULE() # defining a cariable of type MODULE
    k = kmodule.lsmod() # generating a list of server's kernel modules
    for i in k :    # iterating over this list
      resultat.data = i #assign each value to a return value
      yield resultat  # return the value 
    
 ############################################################
 #                                                          #
 # Running Modules  command                                 #
 #  -4                                                      #
 ############################################################
  def RUNNING_MODULES(self, request, context): #displaying the running kernel modules
    
    print(request)
    running_modules = list(km.loaded()) # create a list of tuples of current loaded modules the first element of each tuple is the module name
    for m in running_modules: # iterate each list element
      resultat_Rmodule = Getter_pb2.MODULE() # define the tye of the return values
      resultat_Rmodule.data = str(m[0])[1::] # convert the module from byte to string  
      yield resultat_Rmodule # return the module name
   ############################################################
 #                                                            #
 # ALL User space kernel Modules                              #         
 #  -5                                                        #
 ##############################################################
  def ALL_USER_SPACE_OBJECTS(self, request, context):  # displaying the user space objects (.Ko files in /lib/modules/<kernel_version>/kernel/...)
    print(request)
    modules  = os.listdir("/lib/modules/"+str(uname.release)+"/kernel/") # List the ko object from the directory
    for module in modules:  # iterate this list 
      module_result = Getter_pb2.MODULE() # for each element in this list create  Module variable and assign the file name as it's return message
      module_result.data = module 
      yield module_result
    

################################################################
#################    SETTER SERVICE    #########################
################################################################

class SetterService(grpc_Setter_pb2.SETTERServicer):
 ############################################################
 #                                                          #
 # Uname Modprobe(module)                                   #
 #  -5                                                      #
 ############################################################

  def MODPROBE(self, request, context): # modprobe command used to load a kernel module
    print("The module is "+ str(request.message) + " loading")
    os.system(f"modprobe {request.message}")  # executiing the command on the recieved module name 
    modeprob_reply = Setter_pb2.REPLY() # preparing the result message
    modeprob_reply.message = f"{request.message}"
    return modeprob_reply

  def REMOVE_MODULE(self, request, context): # Unloading linux kernel module from the kernel using the modprobe command
    print("The module will be  "+ str(request.message) + " removed") 
    os.system(f"modprobe -r {request.message}") # executing the command to remove the module
    modeprob_reply = Setter_pb2.REPLY() # creating a reply object type REPLY
    #modeprob_reply.message = f"{os.system('modprobe -r --first-time {request.message}')}" # assigning a verification message to the result message
    modeprob_reply.message = str(os.system("modprobe -r --first-time " + str(request.message))) # assigning a verification message to the result message
    return modeprob_reply
  
    


    

    

    
    
################################################################
#################    RUNNING THE SERVER   ######################
################################################################

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  grpc_Getter_pb2.add_GETTER_INFORMATIONServicer_to_server(GetterService(),server)
  grpc_Setter_pb2.add_SETTERServicer_to_server(SetterService(),server)

  server.add_insecure_port("[::]:50051")
  print("Listening on port 50051")
  server.start()
  server.wait_for_termination()


  ## main function
if __name__ =="__main__":
  serve()