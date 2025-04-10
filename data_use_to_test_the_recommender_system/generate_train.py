import os

image_files = []
#os.chdir(os.path.join("/content/gdrive/MyDrive/FYP/output/images/train"))
for filename in os.listdir("D:\\food\\new_image_test\\train"):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_files.append("D:\\food\\new_image_test\\train\\" + filename)

with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
