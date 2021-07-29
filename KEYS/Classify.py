"""
PSIT Pair-Programming (19th October 2017)
#1 - Supakit Theanthunyakit (it60070098)
#2 - Teerapat Kraisrisirikul (it60070183)
"""
 
def main():
    """ Main function """
    students = dict()
    while True:
        info = input()
        if info == 'END':
            break
        #Add student count
        if (int(info[0:2]), int(info[2:4])) in students:
            #If the data already exist.
            students[(int(info[0:2]), int(info[2:4]))] += 1
        else:
            #If the data is new.
            students[(int(info[0:2]), int(info[2:4]))] = 1
 
    #Output
    year_prev = None
    for year, faculty in sorted(students):
        print("--" if year == year_prev else year, end=' ') #Print "--" or year
        print(faculty, students[(year, faculty)])           #Print the rest of data
        year_prev = year
 
main()