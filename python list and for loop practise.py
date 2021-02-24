#step 1

beatles=[]

#step2

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

#step3

for i in range(2):
  beatles.append(input("\nAdd 'Stu Sutcliffe' and 'Pete Best' to the list(one name at a time):  "))

  '''question wasn't clear but it asked to PROMPT THE USER to ADD the following members of the list so that's what i did.'''

#step4

del beatles[3: 5]

#step5

beatles.insert(0,"Ringo Starr")

print(beatles)
