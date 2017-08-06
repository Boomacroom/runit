import shlex, platform, time, psycopg2
from subprocess import STDOUT, check_output

def checkDB():
    try:
        print('Connecting to Database:')
        connect_str = "dbname='amazon' user='postgres' host='dealfinder.ga' " + \
                      "password='Packard84' port='5433'"
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()
        execstr = 'SELECT program, runorkill, changed FROM programs;'
        cursor.execute(execstr)
        rows = cursor.fetchall()
        print('Connected Successfully! Checking for commands..')
    except Exception as e:
        print("Uh oh, can't connect. Can you access the server via other means?")
        print(e)
    try:
        for row in rows:
            programName = row[0]
            run = row[1]
            changed = row[2]
            print(programName, run)

            if run == True and changed == True:
                print("Running {}...".format(programName))
                cmd = shlex.split("python {}".format(programName))
                output = check_output(cmd, stderr=STDOUT)
                print(output)
            elif run == True and changed == False:
                print('No Changes dectected, waiting 60 Seconds to check again..')
            elif run == False:
                #Terminate
                pass
            else:
                print("Terminating {}...".format(programName))
    except Exception as e:
        print("Unable to check for program execution..")
        print(e)

def main():
    operatingSystem = platform.system()

    # Detect what OS we are running on:
    if operatingSystem == "Windows":
        print("Not implemented for Windows OS yet.. Although \
the current code will also work for Windows")
        pass
    #TODO: This needs to be changed to Linux, dev on Windows so it's just for testing
    elif operatingSystem == "Linux":
        starttime = time.time()
        while True:
            print ("Detecting Changes..")
            checkDB()
            time.sleep(60.0 - ((time.time() - starttime) % 60.0))

if __name__ == "__main__":
    main()