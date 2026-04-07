import psutil


allowed_processes = [
"System Idle Process",
"System",
"Registry",
"smss.exe",
"csrss.exe",
"wininit.exe",
"winlogon.exe",
"services.exe",
"lsass.exe",
"fontdrvhost.exe",
"svchost.exe",
"dwm.exe",
"VBoxService.exe",
"Memory Compression",
"MsMpEng.exe",
"sihost.exe",
"taskhostw.exe",
"ctfmon.exe",
"NisSrv.exe",
"explorer.exe",
"SearchIndexer.exe",
"StartMenuExperienceHost.e",
"RuntimeBroker.exe",
"SearchApp.exe",
"smartscreen.exe",
"SecurityHealthSystray.exe",
"VBoxTray.exe",
"SecurityHealthService.exe",
"ShellExperienceHost.exe",
"TrustedInstaller.exe",
"TiWorker.exe",
"ApplicationFrameHost.exe",
"dllhost.exe",
"SgrmBroker.exe",
"WinStore.App.exe",
"dasHost.exe",
"TextInputHost.exe",
"SystemSettings.exe",
"SystemSettingsAdminFlows.",
"audiodg.exe",
"WmiPrvSE.exe",
"conhost.exe",
"VSSVC.exe",
"SearchProtocolHost.exe",
"SearchFilterHost.exe",
"osk.exe",
"tasklist.exe"

]

import os
import shutil

def clear_startup_folder():
    
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    
    files_in_startup = os.listdir(startup_folder)

    
    for file_name in files_in_startup:
        file_path = os.path.join(startup_folder, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Removed: {file_name}")
        except Exception as e:
            print(f"Error while removing {file_name}: {e}")


clear_startup_folder()



all_processes = psutil.process_iter(attrs=['name'])


for process in all_processes:
    if process.info['name'] not in allowed_processes:
        try:
            
            process.kill()
            print(f"Killed process: {process.info['name']}")
        except Exception as e:
            print(f"Failed to kill {process.info['name']}: {e}")
