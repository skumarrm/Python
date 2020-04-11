provider "aws" {
  profile    = "default"
  region     = "${var.region}"
}

resource "aws_instance" "myFirst_Terraform_Instance" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
  tags {
        Name = "${var.ec2-instance-name}"
	   }
}
