import sys,semid
sys.argv.pop(0)
if len(sys.argv) < 1:
    semid.__app__.start()
else:
    semid.__app__.start(sys.argv)
