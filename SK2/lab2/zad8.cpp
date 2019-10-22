#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <iostream>
#include <unistd.h>
#include <ctype.h>

#define BUF_SIZE 16

int main(int argc, char* argv[]) {
    sockaddr_in address = {AF_INET, htons(8081), INADDR_ANY};

    int fd = socket(AF_INET, SOCK_DGRAM, 0);

    if (bind(fd, (sockaddr *) &address, sizeof(address)) == -1) {
        perror("Bind Error");
    }

    sockaddr_in client_address{};
    socklen_t size_cl_addr = sizeof(client_address);

    char buf[BUF_SIZE];

    int size = recvfrom(fd, buf, BUF_SIZE, 0, (sockaddr *) &client_address, &size_cl_addr);
    for(char *it=buf; (*it=toupper(*it)); ++it);
    sendto(fd, buf, size, 0, (sockaddr *) &client_address, sizeof(client_address));

    close(fd);
}
    