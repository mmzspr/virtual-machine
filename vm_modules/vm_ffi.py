ffi_library = "./ffi/library.so"

ffi_cdef = r'''
void print(char* str);
short int* key_windows(void);
int unix_time(void);
'''

ffi_list = [
    {"name": "print", "arg_n": 1, "return": False, "result_len": 0},
    {"name": "unix_time", "arg_n": 0, "return": True, "result_len": 0},
    {"name": "key_windows", "arg_n": 0, "return": True, "result_len": 256},
]