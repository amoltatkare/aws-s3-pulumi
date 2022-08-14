"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

config = pulumi.Config()
data = config.require_object("data")
bucketname = data.get("bucket_name")
bucketacl = data.get("acl")

print (bucketname + " : " + bucketacl)

bucket = aws.s3.Bucket("bucket",
    acl=bucketacl,
    tags={
        "Name": bucketname
    })

pulumi.export('id', bucket.id)
pulumi.export('region', bucket.region)
