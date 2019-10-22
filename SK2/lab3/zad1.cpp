#include <unistd.h>
#include <thread>
#include <arpa/inet.h>
#include <netdb.h>
    
int main() {
    
    std::thread t1([&]{
        sleep(1);
        gethostbyname("spam.org");
    });
    
    std::thread t2([&]{
        hostent* ret = gethostbyname("fc.put.poznan.pl");
        sleep(2);
        printf("%s: %s\n", ret->h_name, inet_ntoa(**(in_addr**)ret->h_addr_list));
    });
    
    t1.join();
    t2.join();    
    return 0;
}

