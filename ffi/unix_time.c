#include <sys/time.h>
#include "function.h"

int unix_time(void) {
    struct timeval te; 
    gettimeofday(&te, NULL);
    int milliseconds = te.tv_sec*1000 + te.tv_usec/1000;
    return milliseconds;
}
