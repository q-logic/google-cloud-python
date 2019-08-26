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


def client_query_destination_table_cmek(client, table_id):

    # [START bigquery_query_destination_table_cmek]
    from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the destination table.
    # table_id = "your-project.your_dataset.your_table_name"

    job_config = bigquery.QueryJobConfig()
    job_config.destination = table_id

    # Set the encryption key to use for the destination.
    # TODO(developer): Replace this key with a key you have created in KMS.
    kms_key_name = "projects/{}/locations/{}/keyRings/{}/cryptoKeys/{}".format(
        "cloud-samples-tests", "us-central1", "test", "test"
    )
    encryption_config = bigquery.EncryptionConfiguration(kms_key_name=kms_key_name)
    job_config.destination_encryption_configuration = encryption_config
    query_job = client.query(
        "SELECT 17 AS my_col;",
        # Location must match that of the dataset(s) referenced in the query
        # and of the destination table.
        location="US",
        job_config=job_config,
    )
    query_job.result()

    table = client.get_table(table_id)
    if table.encryption_configuration.kms_key_name == kms_key_name:
        print("The destination table is written using the encryption configuration")
    # [END bigquery_query_destination_table_cmek]
