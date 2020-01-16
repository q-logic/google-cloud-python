# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def extract_table(table_id):

    # [START bigquery_extract_table]
    from google.cloud import bigquery
    from google.cloud import storage

    import time

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Construct a Storage client object.
    storage_client = storage.Client()

    # TODO(developer): Set table_id to the ID of the model to fetch.
    # table_id = 'your-project.your_dataset.your_table'

    bucket_name = "extract_shakespeare_{}".format(int(time.time() * 1000))
    bucket = storage_client.create_bucket(bucket_name)

    destination_uri = "gs://{}/{}".format(bucket_name, "shakespeare.csv")

    table = bigquery.Table(
        table_id,
        schema=[
            bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
        ],
    )
    table = client.create_table(table)

    extract_job = client.extract_table(
        table,
        destination_uri,
        # Location must match that of the source table.
        location="US",
    )  # API request
    extract_job.result()  # Waits for job to complete.

    print(
        "Exported {}.{}.{} to {}".format(
            table.project, table.dataset_id, table.table_id, destination_uri
        )
    )
    # [END bigquery_extract_table]

    blob = bucket.get_blob("shakespeare.csv")
    return blob, bucket
