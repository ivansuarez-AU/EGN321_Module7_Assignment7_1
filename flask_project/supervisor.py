import subprocess, sys, time
while True:
    print("SUPERVISOR: starting app")
    p = subprocess.Popen([sys.executable,"app.py"])
    code = p.wait()
    print("SUPERVISOR: app exited",code)
    time.sleep(1)