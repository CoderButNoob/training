def reverse():
    
    input_file = input("Enter path")

    with open(input_file , "r") as i:
        lines = i.readlines()
        print(lines)

    reverse_line = []
    for line in lines :
        rev = ' '.join(line.strip().split()[::-1])
        reverse_line.append(rev)

    output_path = input_file.replace(".txt","reversed.txt")

    with open(output_path, "w") as output:
        output.writelines(reverse_line)


if __name__ == "__main__":
    reverse()


    
