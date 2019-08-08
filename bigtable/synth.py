# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
from synthtool import gcp

gapic = gcp.GAPICGenerator()
common = gcp.CommonTemplates()

# ----------------------------------------------------------------------------
# Generate bigtable and bigtable_admin GAPIC layer
# ----------------------------------------------------------------------------
library = gapic.py_library(
    "bigtable",
    "v2",
    config_path="/google/bigtable/artman_bigtable.yaml",
    artman_output_name="bigtable-v2",
    include_protos=True,
)

s.move(library / "google/cloud/bigtable_v2")
s.move(library / "tests")

# Generate admin client
library = gapic.py_library(
    "bigtable_admin",
    "v2",
    config_path="/google/bigtable/admin/artman_bigtableadmin.yaml",
    artman_output_name="bigtable-admin-v2",
    include_protos=True,
)

s.move(library / "google/cloud/bigtable_admin_v2")
s.move(library / "tests")

s.replace(
    [
        "google/cloud/bigtable_admin_v2/gapic/bigtable_instance_admin_client.py",
        "google/cloud/bigtable_admin_v2/gapic/bigtable_table_admin_client.py",
    ],
    "'google-cloud-bigtable-admin'",
    "'google-cloud-bigtable'",
)

s.replace(
    "google/**/*.py",
    "from google\.cloud\.bigtable\.admin_v2.proto",
    "from google.cloud.bigtable_admin_v2.proto",
)

s.replace(
    ["google/cloud/bigtable_admin_v2/__init__.py"],
    "    __doc__ = bigtable_instance_admin_client."
    "BigtableInstanceAdminClient.__doc__\n",
    "    __doc__ = (\n"
    "        bigtable_instance_admin_client.BigtableInstanceAdminClient."
    "__doc__)\n",
)

s.replace(
    ["google/cloud/bigtable_v2/gapic/bigtable_client.py"],
    "if ``true_mutations`` is empty, and at most\n\n\s*100000.",
    "if ``true_mutations`` is empty, and at most 100000.",
)

s.replace(
    ["google/cloud/bigtable_v2/gapic/bigtable_client.py"],
    "if ``false_mutations`` is empty, and at most\n\n\s*100000.",
    "if ``false_mutations`` is empty, and at most 100000.",
)

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(unit_cov_level=97, cov_level=99)
s.move(templated_files, excludes=['noxfile.py'])

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
