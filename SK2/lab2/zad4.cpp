#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <iostream>
#include <unistd.h>

int main(int argc, char* argv[]) {
    sockaddr_in address = {AF_INET, htons(8081), INADDR_ANY};
    sockaddr_in in_addr;
    socklen_t len_in_addr = sizeof(in_addr);

    int fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    
    if (bind(fd, (sockaddr *) &address, sizeof(address)) == -1) {
        perror("Przy bindowaniu");
    } else {
        listen(fd, SOMAXCONN);
        int c1 = accept(fd, (sockaddr *) &in_addr, &len_in_addr);
        char buf[16] = "abcdef";
        write(c1, buf, 16);
        shutdown(c1, SHUT_RDWR);
    }

    close(fd);

    return 0;
}
