import random
import os

game_status = 'restart'
while (game_status == 'restart'):
    word_dict= {}
    index=0
    correct_word_list=[]
    mystery_word_list=[]
    guessed_list=[]
    junk_list=[]
    alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    guesses_remaining= 6
    
   
    def six_remaining():
        print("  ________")
        print(" |        |")
        print(" |        |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    def five_remaining():
        print("  ________")
        print(" |        |")
        print(" |        |")
        print(" |        O")
        print(" |")
        print(" |")
        print("_|_")
    def four_remaining():
        print("  ________")
        print(" |        |")
        print(" |        |")
        print(" |        O")
        print(" |        |")
        print(" |")
        print("_|_")
    def three_remaining():
        print("  ________")
        print(" |        |")
        print(" |        |")
        print(" |        O")
        print(" |       -|")
        print(" |")
        print("_|_")
    def two_remaining():
        print("  ________")
        print(" |        |")
        print(" |        |")
        print(" |        O")
        print(" |       -|-")
        print(" |")
        print("_|_")
    def one_remaining():
        print("  ________")
        print(" |        |")
        print(" |        |")
        print(" |        O")
        print(" |       -|-")
        print(" |      _/ ")
        print("_|_")
    def none_remaining():
        print("  ________")
        print(" |        |")
        print(" |        |")
        print(" |        O")
        print(" |       -|-" )
        print(" |      _/ \_")
        print("_|_")
        
    
    #def my_func(game_start):
    open_words = open('words.txt')
    for word in open_words:
      if len(word) > 1:
          word_strip=word.strip().lower()
          word_dict[index]=word_strip
          index+=1
    
    num= random.randint(0, len(word_dict))
    mystery = word_dict[num]
    for char in mystery:
      mystery_word_list.append(char)
      correct_word_list.append(' ')
    
    print('this word has %d letters' %len(correct_word_list)) 
    print(correct_word_list)
    #print(mystery)
    def get_matches(user_input, mystery_word_list):
      matches=[]
      indx = 0
      if user_input in mystery_word_list:
        for element in mystery_word_list:
          if user_input == element:
            matches.append(indx)
          indx +=1
      return matches
    
    def update_correct_word_list(matches, correct_word_list, user_input):
      for match in matches:
        correct_word_list[match]=user_input
    
    def update_board(letters):
      print(' ')
      for letter in letters:
        print(letter, end= ' ')
      print(' ')
      
    def catch_errors():
      if user_input not in alphabet:
       print('invalid input, guess a letter from the alphabet.')
       junk_list.append(user_input)
      if user_input in guessed_list:
        print('you already guessed this!')
        junk_list.append(user_input)
       
    update_board(letters)
    while guesses_remaining > 0:
      if guesses_remaining == 6:
        six_remaining()
      if guesses_remaining == 5:
        five_remaining()
      if guesses_remaining == 4:
        four_remaining()
      if guesses_remaining == 3:
        three_remaining()
      if guesses_remaining == 2:
        two_remaining()
      if guesses_remaining == 1:
        one_remaining()
      if guesses_remaining == 0:
        none_remaining()
      print('--------------------------')
      user_input = input('guess a letter: ')
      os.system('cls')
      print('--------------------------')
    
      matches = get_matches(user_input, mystery_word_list)
      
      if user_input not in mystery:
        if user_input in alphabet:
            if user_input not in guessed_list:
                guessed_list.append(user_input)
        
      if user_input in letters:
        letters.remove(user_input)
        update_board(letters)
      else:
        catch_errors()
    
      if len(matches) > 0:
        update_correct_word_list(matches, correct_word_list, user_input)
        print('CORRECT! %s is in the word. ' %(user_input))
        if len(guessed_list) >0:
            print(guessed_list)
        print(correct_word_list)
    
      elif user_input in alphabet:
        guesses_remaining -= 1
        print('WRONG! you have %d guesses remaining! %s is not in the word! ' %(guesses_remaining, user_input))
        if len(guessed_list) >0:
            print(guessed_list)
        print(correct_word_list)
      
      if correct_word_list == mystery_word_list: 
        print('You won!')
        break
      elif guesses_remaining == 0:
        print('You lost!')
        print('The word was... %s ' %(mystery))
    open_words.close()
    
    game_status = input('Type "restart" if you want to play again. Type anything else to quit: ')
