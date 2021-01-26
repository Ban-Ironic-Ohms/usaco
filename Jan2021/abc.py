cowph = input() #'abcdefghijklmnopqrstuvwxyz'
heheard = input() #'mood'

alph = []
heard = []
for i in cowph:
    alph.append(i)
for i in heheard:
    heard.append(i)

count = 0

for i in range(len(heard)):
    heard_letter = heard[i]
    #print(f"heard {heard_letter}")
    try:
        next_letter = heard[i + 1]
        #print(f"the next is {next_letter}")
        if alph.index(heard_letter) >= alph.index(next_letter):
            #print(f"We are adding one!")
            count += 1

    except IndexError:
        count += 1
        print(count)