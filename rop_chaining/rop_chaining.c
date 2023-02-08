#include <stdio.h>  // For puts and fgets
#include <unistd.h> // For execve
#include <stdlib.h>

void access_vault(int code)
{
  if (code == 1337) {
    execve("/bin/sh", NULL, NULL);
  } else {
    puts("Access denied!");
  }
}

int main()
{
  char input_buffer[16];
  puts("Enter the password to access Santa Ono's secret vault:");

  fgets(input_buffer, 64, stdin); // Nothing can go wrong here right?

  return EXIT_SUCCESS;
}
