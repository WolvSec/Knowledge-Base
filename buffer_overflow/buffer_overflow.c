#include <stdio.h>  // For puts and fgets
#include <unistd.h> // For execve
#include <stdlib.h>

void access_vault()
{
  puts("Access granted");
  execve("/bin/sh", NULL, NULL);
}

void get_password()
{
  char input_buffer[16];
  puts("Enter the password to access Santa Ono's secret vault:");

  fgets(input_buffer, 64, stdin); // Nothing can go wrong here right?
}

int main()
{
  get_password();

  puts("HAHA you thought! There was no password, you can NEVER get in >:)");

  return EXIT_SUCCESS;
}
