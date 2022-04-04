# f = [(15, {'EventHeader': {'Size': 128, 'HeaderType': 0, 'Flags': 576, 'EventProperty': 0,
# 'ThreadId': 11364, 'ProcessId': 11092, 'TimeStamp': 132635050005504896,
#
# 'ProviderId':
# '{EDD08927-9CC4-4E65-B970-C2560FB5C289}',
#
# 'EventDescriptor':
# {'Id': 15, 'Version': 1, 'Channel': 16, 'Level': 4, 'Opcode': 0, 'Task': 15, 'Keyword': 9223372036854776096},
# 'KernelTime': 41, 'UserTime': 104, 'ActivityId': '{00000000-0000-0000-0000-000000000000}'},
#
# 'Task Name': 'READ', 'ByteOffset': '0x335', 'Irp': '0xFFFF818599569888', 'FileObject': '0xFFFF81859EFC53F0',
# 'FileKey': '0xFFFFC401DFC29830', 'IssuingThreadId': '11364', 'IOSize': '0x200', 'IOFlags': '0x0',
# 'ExtraFlags': '0x0', 'Description': ''}), (15, {'EventHeader': {'Size': 128, 'HeaderType': 0, 'Flags': 576, 'EventProperty': 0,
# 'ThreadId': 11364, 'ProcessId': 11092, 'TimeStamp': 132635050005504896,
#
# 'ProviderId':
# '{EDD08927-9CC4-4E65-B970-C2560FB5C289}',
#
# 'EventDescriptor':
# {'Id': 15, 'Version': 1, 'Channel': 16, 'Level': 4, 'Opcode': 0, 'Task': 15, 'Keyword': 9223372036854776096},
# 'KernelTime': 41, 'UserTime': 104, 'ActivityId': '{00000000-0000-0000-0000-000000000000}'},
#
# 'Task Name': 'READ', 'ByteOffset': '0x335', 'Irp': '0xFFFF818599569888', 'FileObject': '0xFFFF81859EFC53F0',
# 'FileKey': '0xFFFFC401DFC29830', 'IssuingThreadId': '11364', 'IOSize': '0x200', 'IOFlags': '0x0',
# 'ExtraFlags': '0x0', 'Description': ''}),(15, {'EventHeader': {'Size': 128, 'HeaderType': 0, 'Flags': 576, 'EventProperty': 0,
# 'ThreadId': 11364, 'ProcessId': 11092, 'TimeStamp': 132635050005504896,
#
# 'ProviderId':
# '{EDD08927-9CC4-4E65-B970-C2560FB5C289}',
#
# 'EventDescriptor':
# {'Id': 15, 'Version': 1, 'Channel': 16, 'Level': 4, 'Opcode': 0, 'Task': 15, 'Keyword': 9223372036854776096},
# 'KernelTime': 41, 'UserTime': 104, 'ActivityId': '{00000000-0000-0000-0000-000000000000}'},
#
# 'Task Name': 'READ', 'ByteOffset': '0x335', 'Irp': '0xFFFF818599569888', 'FileObject': '0xFFFF81859EFC53F0',
# 'FileKey': '0xFFFFC401DFC29830', 'IssuingThreadId': '11364', 'IOSize': '0x200', 'IOFlags': '0x0',
# 'ExtraFlags': '0x0', 'Description': ''}),]
#
#
# from Serializer import Serializer
# ser = Serializer()
# ser.serialize("test1.json", f)
# f = ser.deserialize("test1.json")
# print(f)
from functools import reduce

s = """OPERATIONEND,24,CLOSE,14,CREATE,12,QUERYSECURITY,32,FSCTL,23,QUERYINFORMATION,22,CLEANUP,13,READ,15,DIRNOTIFY,25,CREATENEWFILE,30,WRITE,16,NAMECREATE,10,SETINFORMATION,17,RENAME,19,RENAMEPATH,27,NAMEDELETE,11,SETDELETE,18,DELETEPATH,26,DIRENUM,20,QUERYEA,34,FLUSH,21,SETSECURITY,31"""
s = s.split(",")
sumx = ""
for i in range(len(s)):
    sumx += ((f"\"{s[i]}\"" if i % 2 == 0 else s[i]) + f": {i},\n")


print(sumx)