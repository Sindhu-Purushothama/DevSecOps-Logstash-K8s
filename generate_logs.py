import time
import random

log_file = "./logs/access.log"

methods = ["GET", "POST", "PUT", "DELETE"]
resources = ["/home", "/login", "/dashboard", "/api/data"]

while True:
    method = random.choice(methods)
    resource = random.choice(resources)
    status = random.choice([200, 201, 400, 401, 403, 404, 500])
    log_line = f'127.0.0.1 - - [01/Sep/2025:10:00:00 +0000] "{method} {resource} HTTP/1.1" {status} 123\n'
    
    with open(log_file, "a") as f:
        f.write(log_line)
    
    time.sleep(1)
