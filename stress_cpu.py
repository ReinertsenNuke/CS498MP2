from flask import Flask, request
from multiprocessing import Pool
from multiprocessing import cpu_count
import socket

app = Flask(__name__)

def stress_cpu(n):
   total = 0
   for i in range(n):
      total += i**2
   return total

start_time = time.time()

processes = cpu_count()
pool = Pool(processes)
print(pool.map(stress_cpu,[110000000,110000000]))
print("time_cost: ", time.time() - start_time)

@app.route('/',methods=['POST'])
def do_post():
   subprocess.Popen("stress_cpu.py")

@app.route('/',methods=['GET'])
   return socket.gethostname()

if __name__ == '__main__'
   app.run(host="0.0.0.0",port=5000)

