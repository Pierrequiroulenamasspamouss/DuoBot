import config
import time
import subprocess
scrcpy_path = config.scrcpy_path 
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