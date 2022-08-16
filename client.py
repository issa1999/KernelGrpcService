from email import message
import Getter.KernelGetterService_pb2 as pb2
import Getter.KernelGetterService_pb2_grpc as grpc_pb2
import Setter.KernelSetterService_pb2 as Setter_pb2
import Setter.KernelSetterService_pb2_grpc as grpc_Setter_pb2 
import grpc 
def run():
    with grpc.insecure_channel("0.0.0.0:50051") as channel:
        stub = grpc_pb2.GETTER_INFORMATIONStub(channel)
        stubb = grpc_Setter_pb2.SETTERStub(channel)
        #print("1-Uname\n2-MODINFO\n3-All_Modules\n4-Current Running Modules \n ")
        #print("5-Current config")
        #print("6-All_Kernel_Object\n7-REMOVE_MODULE\n8-DEPLOY_MODULE\n9-INSTALL_KERNEL_OBJECT\n10-Modprobe ")
        print("1-UNAME")
        print("2-MODINFO")
        print("3-ALL_MODULES")
        print("4-ALL_RUNNING_MODULE")
        print("5-KERNEL_OBJECT_LIST")
        print("6-CURRENT_KERNEL_CONFIG")
        print("7-REMOVE_MODULE")
        print("8-DEPLOY A MODULE / INSTALL .KO FILE")
        print("9-LOAD A MODULE")
        print("Your choice :")
        choice = int(input())

        if choice == 1: # display general kernel informations ( uname Unix command )
            uname_request = pb2.MODULE()
            uname_reply = stub.UNAME(uname_request)
            print(uname_reply)
        elif choice == 2:  # modinfo(module) ==> ['info':'value']
            print("Enter a module name \t")
            module_to_display = input()  # enter the module name to display its informations
            modinfo_request = pb2.MODULE(data = module_to_display)  # set the module name as the request.data value ( which will be sent to the server)
            modinfo_replies = stub.MODINFO(modinfo_request)  # get the list of responses from the server ( list of module infos)
            for modinfo_reply in modinfo_replies: # iterate each item and print it
                print(modinfo_reply)

        elif choice == 3: # display all kernel modules (ALL_MODULE)
            all_module_request = pb2.MODULE()
            all_module_reply = stub.ALL_MODULES(all_module_request)
            for module in all_module_reply : 
                print(module)
          #  all_modules_request = pb2.MODULE()
          #  all_modules_reply = stub.ALL_MODULES(all_modules_request)
          #  for i in all_modules_reply:
          #      print(all_modules_reply)
        elif choice == 4: # display all running modules found in the file /proc/modules (CURRENT_RUNNING_MODULES)
            print("current running modules are : \n") 
            running_modules_request = pb2.MODULE()  #create a Module object for the request
            running_modules_replies = stub.RUNNING_MODULES(running_modules_request) # creating a list for the running modules
            for run_mod in running_modules_replies: # iterate the return list and print the results
                print(run_mod)
        elif choice == 5: #ALL_KERNEL_OBJECT_LIST
            all_kernel_object_request = pb2.MODULE() # create a module object for the request 
            all_kernel_object_results = stub.ALL_USER_SPACE_OBJECTS(all_kernel_object_request) # create a list for the result ( result pf execution of the function on the server)
            for ko_obj in all_kernel_object_results: # iterate the result and print them
                print(ko_obj)
           # module_to_modprobe = input("Enter the module name :")
           # module_to_modprobe_request = Setter_pb2.REQUEST(message = module_to_modprobe)
           # module_to_modprobe_reply = stubb.MODPROBE(module_to_modprobe_request)
           # print(module_to_modprobe_reply)
           # print(module_to_modprobe)
        elif choice == 6:# display current config
            current_config_request = pb2.MODULE()
            current_config_replies = stub.CURRENT_CONFIG(current_config_request) # creating a list for the running modules
            for current_config_reply in current_config_replies: # iterate the return list and print the results
              print(current_config_reply)


        elif choice ==7: #remove a module / unload a module
            module_to_unload = input("Enter the module name") # the module to unload
            module_to_unload_req = Setter_pb2.REQUEST(message = module_to_unload) # tell the server which module to unload
            module_to_unload_res = stubb.REMOVE_MODULE(module_to_unload_req) # execute the unload function on the server 
            print(module_to_unload_res) # print the result message 
        elif choice == 8: # DEPLOY A MODULE / INSTALL A KO OBJECT
            module_to_deploy = input("PLease enter the KO file path")
            module_to_deploy_req = Setter_pb2.REQUEST(message = module_to_deploy)
            module_to_deploy_rep = stubb.DEPLOY_MODULE(module_to_deploy_req)
            print(module_to_deploy_rep)
        elif choice == 9:   #LOAD A MODULE
            module_to_load = input("Enter a module name") # the module to load
            module_to_load_req = Setter_pb2.REQUEST(message = module_to_load) # create a module pbj to announce to the server the name of the module to load
            module_to_load_res = stubb.MODPROBE(module_to_load_req) # execute the function on the module to load and save the results
            print(module_to_load_res) # print the result 


if __name__=="__main__":
    run()

 