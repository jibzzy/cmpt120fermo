# avg.2py
#   A simple program to average two exam scores
#   Illustrates use of multiple input
def main():
    print("This program computes the average of three exam scores.")
    score1, score2, score3 = eval(input("Input your three scores here"))
    average = (score1 + score2 + score3) / 3
    print("The average of the scores is", average)

main()
