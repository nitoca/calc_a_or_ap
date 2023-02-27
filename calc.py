# csvから読み込んで計算する

import csv
import sys

def main():
    # open csv file
    f = open(sys.argv[1], 'r')
    reader = csv.reader(f)
    # skip header
    header = next(reader)
    
    gpa = 0
    ratio_of_a_ap = 0
    ratio_of_ap = 0
    # define enum type for grade
    class Grade:
        Ap_g = 4.3
        A_g = 4
        B_g = 3
        C_g = 2
        D_g = 0
    # calc ratio of A and A+

    all_credit = 0

    for row in reader:
        # calc all credit
        # row[4] convert to int
        all_credit += float(row[4])

        # calc gpa
        if row[7] == 'A+':
            gpa += Grade.Ap_g * float(row[4])
        elif row[7] == 'A':
            gpa += Grade.A_g * float(row[4])
        elif row[7] == 'B':
            gpa += Grade.B_g * float(row[4])
        elif row[7] == 'C':
            gpa += Grade.C_g * float(row[4])
        elif row[7] == 'D':
            gpa += Grade.D_g * float(row[4])

        # calc ratio of A and A+
        if row[7] == 'A+':
            ratio_of_ap += float(row[4])
            ratio_of_a_ap += float(row[4])
        elif row[7] == 'A':
            ratio_of_a_ap += float(row[4])


    # calc gpa
    gpa /= all_credit
    # calc ratio of A and A+
    ratio_of_a_ap /= all_credit
    ratio_of_ap /= all_credit
    

    print('対象外科目も含むGPA: ' + str(gpa))
    print('Ratio of A and A+: ' + str(ratio_of_a_ap))
    print('Ratio of A+: ' + str(ratio_of_ap))



if __name__ == '__main__':
    main()