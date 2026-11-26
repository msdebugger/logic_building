"""
Q101: File Type Check
Take a filename as input (like report.pdf). Check if it ends with .pdf, .docx, or .txt and print the file type.
"""
filename = input("Enter filename: ")

if filename.endswith(".pdf"):
    print("PDF File")
elif filename.endswith(".docx"):
    print("DOCX File")
elif filename.endswith(".txt"):
    print("TXT File")
else:
    print("Unknown file type")