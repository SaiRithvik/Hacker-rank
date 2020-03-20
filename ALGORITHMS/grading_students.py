def grading_students():

	
	n = int(input())
	grades =[]
	for i in range(n):

		s = int(input())
		grades.append(s)

	for i in range(0 , n):

		if((grades[i])<38):
			grades[i] = grades[i]

		elif(((int(grades[i])//5+1)*5)-int(grades[i])<3):

			grades[i] = (int((grades[i]))//5+1)*5

	for j in range(0 , n):
		print(grades[j])	

grading_students()		




