import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "6Jf7Dl6Ri3n6wpbce-Sogi4NfGDRdzmvgVYjgjyHMN5iSNnEHXwNB4QIscpQ9yRN8VqQbWbNGuoWFafsbqFZUA=="
org = "race-teller"
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket = "29er"

# write_api = write_client.write_api(write_options=SYNCHRONOUS)
#
# for value in range(5):
#     point = (
#         Point("measurement1")
#         .tag("tagname1", "tagvalue1")
#         .field("field1", value)
#     )
#     write_api.write(bucket=bucket, org="race-teller", record=point)
#     time.sleep(1)  # separate points by 1 second

query_api = client.query_api()

query = "from(bucket: \"29er\") |> range(start: 2000-08-28T22:00:00Z)"
tables = query_api.query(query, org="race-teller")

for table in tables:
    for record in table.records:
        print(record)
#
#
# query = """from(bucket: \"29er\")
#  |> range(start: -10m)
#  |> filter(fn: (r) => r._measurement == "measurement1")"""
# tables = query_api.query(query, org=org)
#
# for table in tables:
#   for record in table.records:
#     print(record)
