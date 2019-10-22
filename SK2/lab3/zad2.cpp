#include <netdb.h>
#include <cstdio>
#include <error.h>
#include <arpa/inet.h>
    
int main(){
    // Ustawienie "podpowiedzi" - sterowanie jakie wyniki chcemy otrzymać:
    addrinfo hints {};
    hints.ai_family   = AF_INET;         // tylko IPv4 (AF_INET)
    hints.ai_protocol = IPPROTO_UDP;     // protokół UDP
    
    // Zmienna w której będzie umieszczona lokalizacja wyniku w pamięci
    addrinfo * resolved;
    
    int res = getaddrinfo("pool.ntp.org", "ntp", &hints, &resolved);
    
    if(res) error(1,0,"Getaddrinfo failed: %s\n", gai_strerror(res));
    if(!resolved) error(1,0,"Empty result\n");
    
    for(addrinfo * it = resolved; it; it=it->ai_next){
        sockaddr_in* addr = (sockaddr_in*) it->ai_addr; // <- rzutowanie bezpieczne,
        printf(" %s\n",inet_ntoa(addr->sin_addr));      //    bo w podpowiedziach 
    }                                                   //    zażądaliśmy adresów IPv4
    
    freeaddrinfo(resolved);
    
    return 0;
}

