#include <string>
#include <iostream>
#include <string_view>

constexpr char KEY = 42;
constexpr std::string_view PHRASE_CIPHERTEXT = "]I^LQREXu^]CIOuCYuDEEZW";

bool is_phrase_correct(std::string_view phrase)
{
  std::string ciphertext{phrase};
  for (char& c : ciphertext)
  {
    c ^= KEY;
  }
  return ciphertext == PHRASE_CIPHERTEXT;
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
