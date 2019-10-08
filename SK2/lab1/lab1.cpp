//
// Created by inf132697 on 08.10.2019.
//

#include "lab1.h"
#include <iostream>
#include <fcntl.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

using namespace std;
int zad1(int argc, char **argv) {
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

int zad6(int argc, char **argv) {
    sockaddr_in address = {AF_INET, htons(13)};
    int fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    address.sin_addr.s_addr = inet_addr("150.254.32.155");
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

int zad7(int argc, char **argv) {
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
