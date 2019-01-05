#include<stdio.h>

/*
    minute
     minut = minut % 60;
     ora = ora + minut / 60; 

    1 ora 50 minute 50 secunde
    1 ora 10 minute 20 secunde
*/

struct time {
    int ora;
    int minut;
    int secunda;
}z1,z2;

struct time timeSum(struct time z1, struct time z2) {
    struct time result;
    
    result.secunda = (z1.secunda + z2.secunda) % 60;

    result.minut = (z1.minut + z2.minut) + (z1.secunda + z2.secunda) / 60;
    result.minut = result.minut % 60;
    
    result.ora = z1.ora + z2.ora + (z1.minut + z2.minut) / 60;

    return result;
}

int main() {

    struct time result;

    z1.ora = 1;
    z1.minut = 30;
    z1.secunda = 15;

    z2.ora = 2;
    z2.minut = 50;
    z2.secunda = 50;

    result = timeSum(z1, z2);

    printf("%d %d %d\n", result.ora, result.minut, result.secunda);
    return 0;
}
