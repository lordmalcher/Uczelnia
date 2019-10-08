#include <iostream>
#include <fcntl.h>
#include <unistd.h>

using namespace std;
int main(int argc, char **argv) {
    int fd = open("test.txt", O_RDONLY);
    if (fd == -1) {
        perror("when opening file");
        return 0;
    }
    char buf[16];
    int count(read(fd, buf, 16));
    write(1, buf, count);

    return 0;
}

