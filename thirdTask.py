marks = input('Ввести оценки за пять опросов(через пробел): ')
marksArray = marks.split(' ')
amountOfMarks = 0
for i in range(marksArray.length):
    amountOfMarks += marksArray[i]
averageMark = amountOfMarks / marksArray.length
