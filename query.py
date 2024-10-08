from influxdb_client_3 import InfluxDBClient3

client = InfluxDBClient3(
    host=f"http://localhost:8086",
    token=f"xAzzOecr5j5geay0YgORfHKzqRjPbE0l2yvgh4D_4EwcvWtjDtLBYEHn4eot0XhAYgffczOlmEycriAaGGll2Q==",
    database=f"29er")

sql = '''
  SELECT
    *
  FROM
    home
  WHERE
    time >= '2024-10-06T08:00:00Z'
    AND time <= '2024-10-06T20:00:00Z'
'''

table = client.query(query=sql)
assert table['room'], "Expect table to have room column."
print(table.to_pandas().to_markdown())
