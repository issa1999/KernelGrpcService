import Getter.KernelGetterService_pb2 as pb2
import Getter.KernelGetterService_pb2_grpc as grpc_pb2
import Setter.KernelSetterService_pb2 as Setter_pb2
import Setter.KernelSetterService_pb2_grpc as grpc_Setter_pb2 
import grpc 
def run():
    with grpc.insecure_channel("0.0.0.0:50051") as channel:
        stub = grpc_pb2.GETTER_INFORMATIONStub(channel)
        stubb = grpc_Setter_pb2.SETTERStub(channel)
        print("1-Uname\n2-MODINFO\n3-All_Modules\n4-Current Running Modules \n ")
        print("5-All_Kernel_Object\n6-REMOVE_MODULE\n7-DEPLOY_MODULE\n8-INSTALL_KERNEL_OBJECT\n9-Modprobe ")
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

        elif choice == 3: # display all kernel modules
            all_modules_request = pb2.MODULE()
            all_modules_reply = stub.ALL_MODULES(all_modules_request)
            for i in all_modules_reply:
                print(all_modules_reply)
        elif choice == 4: # display all running modules found in the file /proc/modules
            print("current running modules are : \n")
            running_modules_request = pb2.MODULE()
            running_modules_replies = stub.RUNNING_MODULES(running_modules_request)
            for run_mod in running_modules_replies:
                print(run_mod)
        elif choice == 5:
            all_kernel_object_request = pb2.MODULE()
            all_kernel_object_results = stub.ALL_USER_SPACE_OBJECTS(all_kernel_object_request)
            for ko_obj in all_kernel_object_results:
                print(ko_obj)
           # module_to_modprobe = input("Enter the module name :")
           # module_to_modprobe_request = Setter_pb2.REQUEST(message = module_to_modprobe)
           # module_to_modprobe_reply = stubb.MODPROBE(module_to_modprobe_request)
           # print(module_to_modprobe_reply)
           # print(module_to_modprobe)
        elif choice == 9:
            module_to_load = input("Enter a module name")
            module_to_load_req = Setter_pb2.REQUEST(message = module_to_load)
            module_to_load_res = stubb.MODPROBE(module_to_load_req)
            print(module_to_load_res)
        elif choice ==6:
            module_to_unload = input("Enter the module name")
            module_to_unload_req = Setter_pb2.REQUEST(message = module_to_unload)
            module_to_unload_res = stubb.REMOVE_MODULE(module_to_unload_req)
            print(module_to_unload_res)







run()