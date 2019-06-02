
def main():
    f1 = input("请输入文件1名： ").strip()
    f2 = input("请输入文件2名： ").strip()

    infile = open(f1, "r")
    outfile = open(f2, "w")

    countLines = countChars = 0
    for line in infile:
        countLines += 1
        countLines += len(line)
        outfile.write(line)
    print(countLines, "Lines and", countChars, "chars copied")

    infile.close()
    infile.close()

main()
