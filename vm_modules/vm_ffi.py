ffi_library = "./ffi/library.so"

ffi_cdef = r'''
void print(char* str);
short int* key_windows(void);
int unix_time(void);
'''

ffi_list = [
    {"name": "print", "return": False, "result_len": 0},
    {"name": "unix_time", "return": True, "result_len": 0},
    {"name": "key_windows", "return": True, "result_len": 256},
]

