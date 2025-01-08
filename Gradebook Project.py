last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print("Gradebook : ", gradebook)

# new grade came in
gradebook.append(["computer science", 100])

print("\nAppended Gradebook : ", gradebook)

# new grade came in
gradebook.append(["visual arts", 93])

print("\nAppended Gradebook 2 : ", gradebook)

# grading error. add 5 pts to vis.arts

gradebook[-1][-1] = gradebook[-1][-1] + 5

print("\nAppended Gradebook 3 : ", gradebook)

# Remove poetry grade

gradebook[2].remove(85)

print("\nAppended Gradebook 4 : ", gradebook)


# add pass/fail to poetry

gradebook[2].append("Pass")

print("\nAppended Gradebook 5 : ", gradebook)


# combine all gradebook

full_gradebook = last_semester_gradebook + gradebook

print("\nFull Gradebook : ", full_gradebook)