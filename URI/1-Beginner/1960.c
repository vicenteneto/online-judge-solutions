#include <stdio.h>
#include <string.h>

/* function declarations */
void convert_units(char number);
void convert_tens(char number);
void convert_hundreds(char number);

int main() {
    char x[5];
    int lnth;

    lnth = strlen(gets(x));

    if(lnth == 3) {
        convert_hundreds(x[0]);
        convert_tens(x[1]);
        convert_units(x[2]);
    } else if(lnth == 2) {
        convert_tens(x[0]);
        convert_units(x[1]);
    } else if(lnth == 1) {
        convert_units(x[0]);
    }

    printf("\n");

    return 0;
}

void convert_units(char number) {
    if(number == '1') printf("I");
    else if(number == '2') printf("II");
    else if(number == '3') printf("III");
    else if(number == '4') printf("IV");
    else if(number == '5') printf("V");
    else if(number == '6') printf("VI");
    else if(number == '7') printf("VII");
    else if(number == '8') printf("VIII");
    else if(number == '9') printf("IX");
}

void convert_tens(char number) {
    if(number == '1') printf("X");
    else if(number == '2') printf("XX");
    else if(number == '3') printf("XXX");
    else if(number == '4') printf("XL");
    else if(number == '5') printf("L");
    else if(number == '6') printf("LX");
    else if(number == '7') printf("LXX");
    else if(number == '8') printf("LXXX");
    else if(number == '9') printf("XC");
}

void convert_hundreds(char number) {
    if(number == '1') printf("C");
    else if(number == '2') printf("CC");
    else if(number == '3') printf("CCC");
    else if(number == '4') printf("CD");
    else if(number == '5') printf("D");
    else if(number == '6') printf("DC");
    else if(number == '7') printf("DCC");
    else if(number == '8') printf("DCCC");
    else if(number == '9') printf("CM");
}
