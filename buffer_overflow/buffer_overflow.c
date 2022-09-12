#include <stdio.h> // for puts and gets
#include <unistd.h>

void access_vault() {
  puts("Access granted");
  execve("/bin/sh", NULL, NULL);
}

int main() {
  char input_buffer[16];
  puts("Enter the password to access Santa Ono's secret vault:");

  fgets(input_buffer, 32, stdin); // Nothing can go wrong here right?

  puts("HAHA you thought! There was no password, you can NEVER get in >:)");

  return 0;
}