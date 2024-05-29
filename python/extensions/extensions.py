def main():

    convert(input("File name ").lower().replace(" ", ""))

def convert(file_name):

    format = file_name.split(".")

    n = len(format)

    if format[n - 1] == "gif":
        print("image/gif")

    elif format[n - 1] == "jpg" or format[n - 1] == "jpeg":
        print("image/jpeg")

    elif format[n - 1] == "png":
        print("image/png")

    elif format[n - 1] == "pdf":
        print("application/pdf")

    elif format[n - 1] == "txt":
        print("text/plain")

    elif format[n - 1] == "zip":
        print("application/zip")

    else:
        print("application/octet-stream\n")

main()

