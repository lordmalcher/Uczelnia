#include <netdb.h>
#include <cstdio>
#include <error.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <iostream>
#include <unistd.h>

int main(int argc, char* argv[]) {
    addrinfo hints{.ai_protocol = IPPROTO_TCP};
    addrinfo * res;

    int response = getaddrinfo("reddit.com", "80", nullptr, &res);

    if (response) {
        error(1,0,"Getaddrinfo failed: %s\n", gai_strerror(response));
    }

    if (!res) {
        error(1,0,"Empty result\n");
    }

    int sock = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
    connect(sock, res->ai_addr, res->ai_addrlen);
    write(sock, "GET / HTTP/1.0\r\n\r\n", 18);

    char buf[512];

    int cnt = read(sock, buf, 512);
    write(1, buf, cnt);

    close(sock);
}
