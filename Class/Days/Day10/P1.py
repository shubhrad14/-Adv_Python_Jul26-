# Process: An independent program with its own memory space.
# 1. Heavy weight
# 2. Separate memory
# 3. Communication is harder

# Thread: A lightweight unit of execution within a process.
# 1. Lightweight
# 2. Shared memory
# 3. Communication is simpler

# Types of tasks
import time

# I/O bound task
def download_file(url):
    print(f"Starting download from {url}")
    time.sleep(2)

    return f"Downloaded: {url}"

# CPU-bound task
def calculate_prime(n):
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

        num +=1

    return num - 1

if __name__ == "__main__":
    result_download = download_file("https://example.com/file")
    print(result_download)

    nth = 1000
    print(f"calculating {nth}th prime...")
    prime_result = calculate_prime(nth)
    print(f" {nth}th prime is : {prime_result}")

    # When to use Threads
    # 1. Web scraping multiple websites
    # 2. Downloading files from the interner
    # 3. Read/write of multiple files
    # 4. Handling multiple network connections
    
    # Bad use case
    # 1. Heavy mathematical computation
    # 2. CPU intensive data processing

    # Concurrency vs Parellelism
    # Multiple tasks make progress over time
    # Tasks are interleaved
    # Single CPU core is shared
    # Looks like they're running simultaneously

    # Parellelism: Mulitiple tasks execure simultaneously
    # Multiple CPU cores
    # Not possible in Python with threads (due to GIL)