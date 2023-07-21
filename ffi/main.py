from cffi import FFI
import time

ffi = FFI()

ffi.cdef(r'''
short int* key_win(void);
double twice(double n);
void print(char* str);
''')

lib = ffi.dlopen('library.so')

def test():
    # _r = ffi.new('double[%d][2]' % n)
    return lib.key_win()

def twice(n):
    # _r = ffi.new('double[%d][2]' % n)
    return lib.twice(n)

def c_print(l):
    # _r = ffi.new('double[%d][2]' % n)
    return lib.print(l)

p = ffi.new("char[]", [b"h",b"e",b"l",b"l",b"o",b"\n"])
c_print(p)
p = ffi.new("char[]", [b"h",b"e",b"l",b"l",b"o",b"\n"])
c_print(p)
p = ffi.new("char[]", b"\033[2A")
c_print(p)
p = ffi.new("char[]", b"hi\n")
c_print(p)
# while True:
#     result = test()
#     for i in range(0, 256):
#         if result[i] == 1:
#             # print(i)
#             print(twice(i))
    # time.sleep(0.01)
