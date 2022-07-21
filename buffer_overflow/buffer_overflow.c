#include <stdio.h> // for puts and gets

void access_vault() { puts("Here is my secret: REDACTED"); }

int main() {
  char input_buffer[16];
  puts("Enter the password to access Santa Ono's secret vault:");

  gets(input_buffer); // Nothing can go wrong here right?

  puts("HAHA you thought! There was no password, you can NEVER get in >:)");

  return 0;
}