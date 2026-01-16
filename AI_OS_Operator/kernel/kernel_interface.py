import subprocess

def get_cpu_load():
    output = subprocess.check_output(
        ["sysctl", "-n", "vm.loadavg"]
    ).decode()

    return float(output.strip("{} ").split()[0])
