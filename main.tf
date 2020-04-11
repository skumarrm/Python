provider "aws" {
  profile    = "default"
  region     = var.region
}

resource "aws_s3_bucket" "my_first_bucket_E146" {
  # NOTE: S3 bucket names must be unique across _all_ AWS accounts, so
  # this name must be changed before applying this example to avoid naming
  # conflicts.
  bucket = "test-bucket-E146"
  acl    = "private"
}

resource "aws_instance" "myFirst_Terraform_Instance" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
  tags = {
        Name = var.ec2-instance-name
       }
  depends_on = [aws_s3_bucket.my_first_bucket_E146]
} 

resource "aws_eip" "ip" {
    vpc = true
    instance = aws_instance.myFirst_Terraform_Instance.id
}
