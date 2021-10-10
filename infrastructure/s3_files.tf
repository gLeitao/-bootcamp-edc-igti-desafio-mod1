resource "aws_s3_bucket_object" "delta_insert" {
  bucket = aws_s3_bucket.dl.id
  key    = "emr-code/pyspark/job_spark.py"
  acl    = "private"
  source = "../etl/job_spark.py"
  etag   = filemd5("../etl/job_spark.py")
}