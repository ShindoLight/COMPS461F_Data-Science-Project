import os

image_files = []
#os.chdir(os.path.join("/content/gdrive/MyDrive/FYP/output/images/train"))
for filename in os.listdir("D:\\food\\new_image_test\\val"):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_files.append("D:\\food\\new_image_test\\val\\" + filename)

with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
