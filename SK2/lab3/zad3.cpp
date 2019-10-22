    #include <netdb.h>
    #include <cstdio>
    #include <error.h>
     
    int main(){
        addrinfo * resolved;
        // Podpowiedzi, port i nazwa hosta są opcjonalne.
        int res = getaddrinfo("ietf.org", nullptr, nullptr, &resolved);
     
        if(res) error(1,0,"Getaddrinfo failed: %s\n", gai_strerror(res));
        if(!resolved) error(1,0,"Empty result\n");
     
        char ip[40]; // maks. długość IP(v6) jako tekst: 8 bloków po 4 znaki oddzielone ':'
        for(addrinfo * it = resolved; it; it=it->ai_next){
            // funkcja getnameinfo tłumaczy dowolny sockaddr na tekst
            res = getnameinfo(it->ai_addr, it->ai_addrlen, ip, 40, nullptr, 0, NI_NUMERICHOST);
            if(res) error(1,0,"Getnameinfo failed: %s\n", gai_strerror(res));
            else printf("%40s (socktype: %d, proto: %d)\n", ip, it->ai_socktype, it->ai_protocol);
        }
     
        freeaddrinfo(resolved);
     
        return 0;
    }

