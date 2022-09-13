#include <string>
#include <iostream>

constexpr auto KEY = 42;

bool is_phrase_correct(std::string_view phrase)
{
  for (char c : phrase)
  {
    std::cout << static_cast<char>(c ^ KEY) << std::endl;
  }
}

int main()
{

  std::string phrase;
  std::cout << "What's the secret phrase?" << std::endl;

  std::getline(std::cin, phrase);

  if (!is_phrase_correct(phrase))
  {
    std::cerr << "Oops try again..." << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "Correct!" << std::endl;

  return EXIT_SUCCESS;
}
