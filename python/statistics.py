print("enter 1 for individual series, 2 for continuos series, 3 for descrete series")
def after_series(series):
    if series == 1 :
        operation_selection = individual()
        return operation_selection
    elif series == 2 :
        operation_selection = continuos()
        return operation_selection
    elif series == 3 :
        operation_selection = descrete()
        return operation_selection
    else:
        print("you enter wrong input")

# individual block
def individual():
     class_list = []
     x = 0
     def in_mean():
         return x/len(class_list)
     
     def in_median():
         class_list.sort()
         median_index = int(term/2)
         if len(class_list)%2!=0:
             return class_list[median_index]
         else:
             return (class_list[median_index-1] + class_list[median_index])/2
         
     def in_mode():
         mode = class_list[0]
         for i in class_list:
             count = class_list.count(i)
             if count > class_list.count(mode):
                 mode = i
         return mode
     
     term = int(input("enter the number of classes : ")) 
     for i in range(term):
         n = eval(input("enter class: "))
         class_list.append(n)
         x = x + n
         
     return in_mean(),in_median(),in_mode()

# continous block
def continuos():
    x = 0
    cf = 0
    lower_list = []
    upper_list = []
    frequency_list = []
    cf_list = []
    n = int(input("enter the number of classes: "))

    def con_mean():
        return x / cf 
    
    def con_median():
        median_index = 0
        N = cf / 2
        for i in range(len(cf_list)):
            if N < cf_list[i] and N > cf_list[i-1] :
                median_index = i
        median = lower_list[median_index] + ((upper_list[median_index]-lower_list[median_index])/frequency_list[median_index])*(N - cf_list[median_index-1])

        return median

    def con_mode():
        f_index = frequency_list.index(max(frequency_list))
        f1 = frequency_list[f_index]
        f2 = frequency_list[f_index+1]
        f0 = frequency_list[f_index-1]
        mode = lower_list[f_index] + ((f1-f0)/((2*f1) - f0 - f2)) * (upper_list[f_index] - lower_list[f_index])
        return mode
    
    for i in range(n):
        print("enter the intervals")
        lower = eval(input("enter the lower limit : "))
        lower_list.append(lower)
        upper = eval(input("enter the upper limit : "))
        upper_list.append(upper)
        frequency = eval(input("enter the frequency : "))
        frequency_list.append(frequency)
        cf = cf + frequency
        cf_list.append(cf)
        x1 = ((upper+lower)/2)*frequency
        x = x + x1

    return con_mean(),con_median(),con_mode()


#  descrete block
def descrete():
    classes_list = []
    frequency_list = []
    cf_list = []
    x = 0
    cf = 0
    classes = int(input("enter the number of classes: "))

    def des_mean():
        return x/cf
    
    def des_median():
        median_index = 0
        N = int((cf+1/2))
        for i in range(len(cf_list)):
            if N < cf_list[i] and N > cf_list[i-1] :
                median_index = i
                print("working")
        median = classes_list[median_index]
        return median     
              
    def des_mode():
        mode_index = frequency_list.index(max(frequency_list))
        return classes_list[mode_index]
        
    for i in range(classes):
        n = eval(input("enter class : "))
        classes_list.append(n)
        frequency = eval(input("enter frequency : "))
        frequency_list.append(frequency)
        x = x + n*frequency
        # print(x)
        cf = cf + frequency
        cf_list.append(cf)
        print(cf)

    return des_mean(),des_median(),des_mode()


series = int(input("enter series: "))
furthur = after_series(series)
print(furthur)