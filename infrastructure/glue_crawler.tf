resource "aws_glue_catalog_database" "dl" {
  name = "desafiodb"
}

resource "aws_glue_crawler" "dl" {
  database_name = aws_glue_catalog_database.dl.name
  name          = "desafio_s3_crawler"
  role          = aws_iam_role.glue_role.arn

  s3_target {
    path = "s3://${aws_s3_bucket.dl.bucket}/staging/"
  }

  configuration = <<EOF
{
   "Version": 1.0,
   "Grouping": {
      "TableGroupingPolicy": "CombineCompatibleSchemas" }
}
EOF

  tags = {
    IES   = "IGTI",
    CURSO = "EDC"
  }
}