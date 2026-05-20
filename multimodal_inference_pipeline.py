import queue
import threading

request_queue = queue.Queue()

def enqueue_request(payload):

    request_queue.put(payload)

def process_requests():

    while not request_queue.empty():

        payload = request_queue.get()

        print(
            f"Processing image diagnosis for {payload['plant_name']}"
        )

def start_pipeline(payloads):

    producer = threading.Thread(
        target=lambda: [
            enqueue_request(payload)
            for payload in payloads
        ]
    )

    consumer = threading.Thread(
        target=process_requests
    )

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
