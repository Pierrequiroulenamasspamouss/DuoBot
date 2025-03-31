import os
import time
import subprocess
scrcpy_path = r"C:\Program Files\scrcpy-win64-v2.7\scrcpy.exe"


def launchscrcpy(slp_time):

    # Vérifie si scrcpy est déjà en cours d'exécution
    for proc in subprocess.run(["tasklist"], capture_output=True, text=True).stdout.splitlines():
        if "scrcpy.exe" in proc:
            print("Scrcpy est déjà en cours d'exécution.")
            time.sleep(slp_time)
            return  # On ne relance pas

    # Lancement du processus en arrière-plan sans bloquer
    subprocess.Popen([scrcpy_path, "-m", "1080", "-f"], shell=False)
    print("Scrcpy lancé en arrière-plan.")

def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False

if __name__ == '__main__':
    launchscrcpy()
    while process_exists('scrcpy.exe'):
        time.sleep(4)