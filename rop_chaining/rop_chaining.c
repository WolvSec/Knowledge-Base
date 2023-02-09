#include <stdio.h>  // For puts and fgets
#include <unistd.h> // For execve
#include <stdlib.h>

void access_vault(int code)
{
  if (code == 1337)
  {
    execve("/bin/sh", NULL, NULL);
  }
  else
  {
    puts("Access denied!");
  }
}

int get_password()
{
  char input_buffer[16];
  puts("Enter the password to access Santa Ono's secret vault:");

  fgets(input_buffer, 64, stdin);

  return atoi(input_buffer);
}

int main()
{
  int password = get_password();

  if (password >= 1000)
  {
    puts("Only authorized personnel can enter numbers greater than 1000!");
    return EXIT_FAILURE;
  }

  access_vault(password);

  return EXIT_SUCCESS;
}
