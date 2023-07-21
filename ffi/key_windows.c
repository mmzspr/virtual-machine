#include <windows.h>
#include "function.h"

short int* key_windows(void) {
    static short int result[256];
    for (int i = 0; i < 256; i++) {
        if(GetAsyncKeyState(i) & 0x8000 ) {
            result[i] = 1;
        }else {
            result[i] = 0;
        }
    }
    return result;
}
