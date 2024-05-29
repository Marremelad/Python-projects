def main():
    var = input("Variable name ")
    convert(var)

def convert(var):
    l = len(var)
    for i in range(l):
        if var[i].isupper():
            split_var = var.split(var[i])
            split_var[0] += "_" + var[i].lower()
            new_var = split_var[0] + split_var[1]
            var = new_var
    print(var)

main()
