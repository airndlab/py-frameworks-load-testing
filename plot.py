import os
import json
import matplotlib.pyplot as plt

base_path = "reports"
apps = ["blacksheep", "fastapi", "muffin", "sanic"]

data = {app: {"users": [], "avg_response_time": [], "p90": [], "p95": [], "error_rate": []} for app in apps}

for app in apps:
    app_path = os.path.join(base_path, app)
    for file_name in os.listdir(app_path):
        if file_name.startswith("result") and file_name.endswith(".json"):
            users = int(file_name.split("-")[2].replace(".json", ""))
            file_path = os.path.join(app_path, file_name)

            with open(file_path, "r") as file:
                report = json.load(file)
                avg_response_time = report["metrics"]["http_req_duration"]["values"]["avg"]
                p90 = report["metrics"]["http_req_duration"]["values"]["p(90)"]
                p95 = report["metrics"]["http_req_duration"]["values"]["p(95)"]
                error_rate = report["metrics"]["http_req_failed"]["values"]["rate"]

                data[app]["users"].append(users)
                data[app]["avg_response_time"].append(avg_response_time)
                data[app]["p90"].append(p90)
                data[app]["p95"].append(p95)
                data[app]["error_rate"].append(error_rate)

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
for app, values in data.items():
    sorted_indices = sorted(range(len(values["users"])), key=lambda i: values["users"][i])
    sorted_users = [values["users"][i] for i in sorted_indices]
    sorted_avg_times = [values["avg_response_time"][i] for i in sorted_indices]
    plt.plot(sorted_users, sorted_avg_times, marker='o', label=app)
plt.title("Avg response time")
plt.xlabel("Users")
plt.ylabel("Avg response time (ms)")
plt.legend(title="Framework")
plt.grid()

plt.subplot(2, 2, 2)
for app, values in data.items():
    sorted_indices = sorted(range(len(values["users"])), key=lambda i: values["users"][i])
    sorted_users = [values["users"][i] for i in sorted_indices]
    sorted_error_rate = [values["error_rate"][i] * 100 for i in sorted_indices]
    plt.plot(sorted_users, sorted_error_rate, marker='o', label=app)
plt.title("Errors")
plt.xlabel("Users")
plt.ylabel("Errors (%)")
plt.legend(title="Framework")
plt.grid()

plt.subplot(2, 2, 3)
for app, values in data.items():
    sorted_indices = sorted(range(len(values["users"])), key=lambda i: values["users"][i])
    sorted_users = [values["users"][i] for i in sorted_indices]
    sorted_p90 = [values["p90"][i] for i in sorted_indices]
    plt.plot(sorted_users, sorted_p90, marker='o', label=app)
plt.title("90th Percentile")
plt.xlabel("Users")
plt.ylabel("90th Percentile (ms)")
plt.legend(title="Framework")
plt.grid()

plt.subplot(2, 2, 4)
for app, values in data.items():
    sorted_indices = sorted(range(len(values["users"])), key=lambda i: values["users"][i])
    sorted_users = [values["users"][i] for i in sorted_indices]
    sorted_p95 = [values["p95"][i] for i in sorted_indices]
    plt.plot(sorted_users, sorted_p95, marker='o', label=app)
plt.title("95th Percentile")
plt.xlabel("Users")
plt.ylabel("95th Percentile (ms)")
plt.legend(title="Framework")
plt.grid()

plt.tight_layout()
plt.show()
