import requests
import time
import statistics
from datetime import datetime
import json


def measure_latency(url, payload, num_requests=10):
    """
    Measure latency of POST requests to an endpoint.

    Args:
        url (str): The endpoint URL
        payload (dict): The JSON payload to send
        num_requests (int): Number of requests to make
    """
    latencies = []
    headers = {'Content-Type': 'application/json'}

    print(f"\nStarting latency test at {
          datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Endpoint: {url}")
    print(f"Number of requests: {num_requests}")
    print("\nMaking requests...")

    for i in range(num_requests):
        try:
            start_time = time.time()
            response = requests.post(url, json=payload, headers=headers)
            end_time = time.time()

            latency = (end_time - start_time) * 1000  # Convert to milliseconds
            status_code = response.status_code
            latencies.append(latency)

            print(f"Request {i+1}: {latency:.2f}ms (Status: {status_code})")

        except requests.exceptions.RequestException as e:
            print(f"Request {i+1} failed: {str(e)}")

    if latencies:
        print("\nResults:")
        print(f"Minimum latency: {min(latencies):.2f}ms")
        print(f"Maximum latency: {max(latencies):.2f}ms")
        print(f"Average latency: {statistics.mean(latencies):.2f}ms")
        print(f"Median latency: {statistics.median(latencies):.2f}ms")
        if len(latencies) > 1:
            print(f"Standard deviation: {statistics.stdev(latencies):.2f}ms")


if __name__ == "__main__":
    # Replace with your endpoint and payload
    endpoint = "https://hjjitof6gb.execute-api.us-east-1.amazonaws.com/Prod/unicorns"
    data = {"Name": "Horsiana", "Weight": 50}
    measure_latency(endpoint, data, num_requests=10)
