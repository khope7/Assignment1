#Task 2: Your Mood Today Ask the user how they feel today. If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!".

#Writing code to print user mood question and ask input
mood = input("How are you doing today? Please type happy or sad. " )

#Conditional statement to catch happy and sad user entries
if mood == "happy":
    print("That's great to hear!")

if mood == "sad":
    print("I hope your day gets better!")