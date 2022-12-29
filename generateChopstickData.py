import uuid
import random

indivds = xrange(1, 100000)
lengths = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]

if __name__ == "__main__":
    fileId = str(uuid.uuid4())
    destFile = fileId + ".txt"
    print "Creating File: " + destFile
    file_object = open(destFile,"a")

    def create_records():
        for y in lengths:
            if (y == 180):
                for x in indivds:
                    randMin = round(random.uniform(19.0, 22.9),2)
                    randMax = round(random.uniform(26.3, 32.5),2)
                    genScore = round(random.uniform(randMin, randMax),2)
                    file_object.write(fileId + "," + str(genScore) + "," + str(x) + "," + str(y) + "\n")
            elif (y == 240):
                for x in indivds:
                    randMin = round(random.uniform(19.1, 22.6),2)
                    randMax = round(random.uniform(27.6, 33.5),2)
                    genScore = round(random.uniform(randMin, randMax),2)
                    file_object.write(fileId + "," + str(genScore) + "," + str(x) + "," + str(y) + "\n")
            elif (y == 230):
                for x in indivds:
                    randMin = round(random.uniform(17.2, 19.9),2)
                    randMax = round(random.uniform(27.5, 32.1),2)
                    genScore = round(random.uniform(randMin, randMax),2)
                    file_object.write(fileId + "," + str(genScore) + "," + str(x) + "," + str(y) + "\n")
            else:
                randMin = round(random.uniform(10.1, 14.3),2)
                randMax = round(random.uniform(19.0, 29.9),2)
                for x in indivds:
                    genScore = round(random.uniform(randMin, randMax),2)
                    file_object.write(fileId + "," + str(genScore) + "," + str(x) + "," + str(y) + "\n")

    if __name__ == "__main__":

        #fake = Factory.create()
        create_records()
        file_object.close()

print "Done!"
