#This code is made by Nathan Brown 6/07/21 this is a te reo quiz made to help users by teaching them basic te reo maaori

import time

print ("Welcome to the te reo quiz what is you're name?")
print ("")

name = input()

print ("")
print ("kia ora " + name)
print ("")
print ("do you know how to play " + name + "?")
print ("")

instrustions_help = input().lower()

print ("")

#if they user has never played before they can ask for instrustions the instrustions will help them and tell them what they might be facing against

if instrustions_help == "yes" or instrustions_help  == "y":
  print ("hope you enjoy and have fun learning " + name + " :)")


elif  instrustions_help == "no"  or instrustions_help == "n" or instrustions_help == "na":
  print ("-------------------------------------------------------")
  print ("okay, this will test you on simple te reo questions " + name + ". if you find the questions to easy there are other level you can play. You will be asked to fill in sentances, spell things correctly and be asked for a simplified definition of the word given to you. There will also be on the 5th question a boss fight on easy, medium will be on the 7th question and 10th question on hard if you answer three question within the time frame (depends what difficulty youve choosen) you will advance to the next difficulty, Are you ready " + name + "?")
  print ("")
  ready = input().lower()
  if ready == "yes" or ready == "y" or ready == "ye":
    print ("")
  elif ready : 
    print("ill give 5 more seconds to read it over then " + name)
    time.sleep (5)

# user will be asked how hard the diffiulty of the questions they want from easy to hard

print ("------------------------------------------------------")

print ("What difficulty do you wish to play on " + name + "?")

chosen_difficulty = input("Easy Medium or Hard.").lower()
# easy difficulty will keep to easy numuracy and vocabuary with hints on each question making them learn new things
if chosen_difficulty == "easy" or  chosen_difficulty == "aesy" :
  print ("-----------------------------------------------")
  print ("")
  print ("Paatai tahi ( Question one )")
  time.sleep (2)
  print ("basic maaori numbers from 1 to 1000s tahi being 1 Tekau being 10 hokorima 100 mano finally being 1000 " + name + " knowing this what number is this rua mano rua tekau ma tahi")
  time.sleep (1)
  print ("")
  print ("A: 2000 20 1")
  print ("B: 2021")
  print ("C: 2011")
  easy_question_1 = input("").lower()
  if easy_question_1 == "a":
    print ("-----------------------------------------")
    print ("thats incorrect if rua = 2 then rua mano would have to mean 2000 because there is 2 of the 1000. " + name + " This also follows for the next part rua tekau that means 20 and the last part tahi meaning one adding them together = 2021")
  if easy_question_1 == "c" :
    print ("-----------------------------------------")
    print ("thats incorrect if rua = 2 then rua mano would have to mean 2000 because there is 2 of the 1000. " + name + " This also follows for the next part rua tekau that means 20 and the last part tahi meaning one adding them together = 2021")
  elif easy_question_1 :
    print ("A, B or C only " + name)
  if easy_question_1 == "b" :
    print ("Thats correct ready for the next question " + name)
    
    readyEQ2 = input().lower()
    if readyEQ2 == "yeah" or readyEQ2 == "ye" or readyEQ2 == "yes" :
      print ("----------------------------------------")
      print ("paatai rua")




if chosen_difficulty == "medium" :
  print ("-----------------------------------------------")