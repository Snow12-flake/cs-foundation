import psutil

def list_processes():
    '''process list code '''
    print("SYSTEM PROCESSES")
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            print(f"PID: {proc.info['pid']:>6} {proc.info['name']:<15} CPU:{proc.info['cpu_percent']:>5.1f}% MEM:{proc.info['memory_percent']:>5.1f}%")
        except:
            pass

def show_system_stats():
    '''stats code'''
    print(f"\nSYSTEM STATS")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1):.1f}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent:.1f}%")

def kill_process():
    '''Kill by PID'''
    pid = input("Enter PID to kill: ")
    try:
        proc = psutil.Process(int(pid))
        proc.kill()
        print(f" Process PID {pid} terminated!")
    except:
        print(f" Failed to kill PID {pid}")

while True:
    print("\nMINI TASK MANAGER")
    print("[L]ist processes  [S]ystem stats  [K]ill process  [Q]uit")
    choice = input("Choose: ").upper()
    
    if choice == 'L':
        list_processes()
    elif choice == 'S':
        show_system_stats()
    elif choice == 'K':
        list_processes() 
        kill_process()
    elif choice == 'Q':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
