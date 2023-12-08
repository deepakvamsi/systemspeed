from multiprocessing import Pool, cpu_count
from datetime import datetime
import platform
import cpuinfo 
import math
from hashlib import sha256

stress_variable = 10000
repeat = 100
os_version = platform.system()
pi = math.pi



def stress_test(args):
    cpu, stress_value = args
    start_time = datetime.now()
    for i in range(repeat):
        for x in range(1,stress_value): 
            add = (float(x) + pi)
            sha256(str(add).encode('utf-8')).hexdigest()
        for x in range(1,stress_value):
            sub = (float(x) - pi)
            sha256(str(sub).encode('utf-8')).hexdigest()
        for x in range(1,stress_value):
            mult = (float(x) *  pi)
            sha256(str(mult).encode('utf-8')).hexdigest()
        for x in range(1,stress_value):
            div = (float(pi) / x)
            sha256(str(div).encode('utf-8')).hexdigest()

    print(f"cpu: {cpu} time: {datetime.now() - start_time}")

if __name__ == '__main__':
    start_time = datetime.now()
    print('Python CPU Benchmark for  (Windows, macOS, Linux)')
    print('CPU: ' + cpuinfo.get_cpu_info().get('brand_raw', "Unknown"))
    print('Arch: ' + cpuinfo.get_cpu_info().get('arch_string_raw', "Unknown"))
    print('OS: ' + str(os_version))
    print('\nBenchmarking: \n')
    cpu_count = cpu_count()
    ### Per CPU how much calculations it can calcualte
    with Pool(cpu_count) as mp_pool:
        mp_pool.map(stress_test, [(cpu, stress_variable) for cpu in range(cpu_count)])
    print(f"total: {datetime.now() - start_time}")
