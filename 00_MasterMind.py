import random

sequence = random.randrange(1000, 10000)

print("Guess the sequence")
print(f"Sequence: {sequence}")

guessSequence = int(input())

if guessSequence == sequence:
    print('hurraaa, you guessed the sequence')

else:
    tries = 0

    while guessSequence != sequence:
        tries =+1
        count = 0

        sequence = str(sequence)
        guessSequence = str(guessSequence)
        
        correct = ['X'] * 4

        for i in range(0,4):
            if (guessSequence[i] == sequence[i]):
                count += 1
                correct[i] = sequence[i]
                #correct.append(sequence[i])
            else:
                continue

        if (count < 4) and (count != 0):
            print(f"you have {count} digits correct")
            #print("also these numbers were even placed correctly: ")

            for k in correct:
                print(k, end=' ')

            print('try again though....')

        guessSequence = int(input())


        if (count == 0):
            print("none of your digits match the sequence...")
            guessSequence = int(input())

    if (sequence == guessSequence):
        tries+=1
        print(f'you are now a mastermind. you used {tries} tries')



        

            

       
