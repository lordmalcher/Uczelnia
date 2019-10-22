#include <iostream>
#include <fcntl.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

using namespace std;
int main(int argc, char **argv) {
    sockaddr_in address = {AF_INET, htons(atoi(argv[2]))};
    int fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    address.sin_addr.s_addr = inet_addr(argv[1]);
    connect(fd, reinterpret_cast<sockaddr *> (&address), sizeof(address));

    char buf[16];
    int count = (read(fd, buf, 16));
    while (count > 0) {
        write(1, buf, count);
        count = (read(fd, buf, 16));
    }

    shutdown(fd, SHUT_RDWR);
    return 0;
}

