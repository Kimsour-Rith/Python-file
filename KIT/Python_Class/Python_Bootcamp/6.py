import statistics

num = int(input('Enter a number: '))
mean1 = statistics.mean(range(1, num+1))
mean2 = statistics.mean([50,75,65,78,98])
mean3 = statistics.mean((65,87,98,785))

print(mean1)
print(mean2)
print(mean3)
@Somphors, The argument you pass in the mean function must be a collection like list, tuple or range like the above code
Vignesh Manoharan10:07 AM
But when you pass an individual integer then you will get error like the below one:

mean = statistics.mean(10)
This mean() is used to get the average of all the numbers not specific to odd or even numbers
