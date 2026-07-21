class SystemFault(Exception): pass      # Changed to uppercase S to keep it clean
class NetworkDrop(SystemFault): pass
class DataCorrupted(SystemFault): pass

try: 

    raise NetworkDrop("[-] SQS connection Lost on Port5432")

except NetworkDrop as error:
    print(f"Executing Network recovery Protocol: {error}")
except DataCorrupted as error:
    print(f"Purging corrupted buffer cache :{error}")
except SystemFault as error:
    print(f"General system failure isolated :{error}")
