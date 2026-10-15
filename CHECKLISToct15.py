#THE TO DO LIST CHECKLIST .
#create a list of 3 tasks :todos ["cleanroom ","do homework ","read book"]
#ask the user to enter the number from 0-2 to choose which task they have finished.
#convert their input into an integer .,change that specific task in the list to the word "DONE".
#print the final updated list .
#step making the to do list .
to_dolist =["clean room","do homework","read book",]
print("current tasks "),to_dolist
choice = int(input("enter the number (0,1,2) according to the number of task you've completed (here 0=1)")) 
to_dolist[choice] = "DONE"

print("updated tasks",to_dolist)

