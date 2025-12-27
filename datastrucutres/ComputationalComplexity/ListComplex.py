import datetime
import random
import time
import os

def main():
    # Use absolute path or verify CWD to ensure we know where the file goes
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ListAccessTiming.xml")
    print(f"Starting ListComplex test. Output will be saved to: {os.path.abspath(filename)}")
    
    # Write an XML file with the results
    with open(filename, "w") as file:
        file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
        file.write('<Plot title="Average List Element Access Time">\n')

        # Test lists of size 1000 to 200000.
        xmin = 1000
        xmax = 200000

        # Record the list sizes in xList and the average access time
        # for 1000 retrievals in yList.
        xList = []
        yList = []

        print("Running list access tests...")
        for x in range(xmin, xmax + 1, 1000):
            xList.append(x)
            
            if x % 10000 == 0:
                print(f"Processing list size: {x}")

            # Creates a list of size x with all 0's
            lst = [0] * x

            # let any garbage collection/memory allocation complete or at least settle down
            # Reduced from 1s to 0.001s which is sufficient for OS scheduler/GC settling
            # without making the script take 3+ minutes.
            time.sleep(0.001)

            # Time before the 1000 test retrievals
            starttime = datetime.datetime.now()

            prod = 0
            for v in range(1000):
                # Find a random location within the list and retrieve a value.
                index = random.randint(0, x - 1)
                val = lst[index]
                prod = prod * val

            # Time after the 1000 test retrievals
            endtime = datetime.datetime.now()

            # The difference in time between start and end in microseconds
            deltaT = endtime - starttime
            accessTime = deltaT.total_seconds() * 1000000
            yList.append(accessTime)

        file.write(' <Axes>\n')
        file.write(f' <XAxis min="{xmin}" max="{xmax}">List Size</XAxis>\n')
        file.write(f' <YAxis min="{min(yList) if yList else 0}" max="60">Microseconds</YAxis>\n')
        file.write(' </Axes>\n')

        file.write(' <Sequence title="Average Access Time vs List Size" color="red">\n')
        for i in range(len(xList)):
            file.write(f' <DataPoint x="{xList[i]}" y="{yList[i]}"/>\n')
        file.write(' </Sequence>\n')

        # This part of the program tests access at 100 random locations within a list
        # of 200,000 elements to see that all the locations can be accessed in
        # about the same amount of time.
        print("Running distribution test...")
        big_list = [0] * 200000
        counts = [0] * 200000
        times = [0.0] * 200000

        time.sleep(0.1)

        for _ in range(100):
            starttime = datetime.datetime.now()
            index = random.randint(0, 200000 - 1)
            big_list[index] += 1
            endtime = datetime.datetime.now()
            deltaT = endtime - starttime
            counts[index] += 1
            times[index] += deltaT.total_seconds() * 1000000

        file.write(' <Sequence title="Access Time Distribution" color="blue">\n')
        for i in range(len(counts)):
            if counts[i] > 0:
                avg = times[i] / counts[i]
                file.write(f' <DataPoint x="{i}" y="{avg}"/>\n')
        file.write(' </Sequence>\n')

        file.write('</Plot>\n')
    
    print("Done! XML file created.")

if __name__ == "__main__":
    main()
