provider "aws" {
  profile    = "default"
  region     = var.region
}

resource "aws_s3_bucket" "my_first_bucket_mmda_colony" {
  # NOTE: S3 bucket names must be unique across _all_ AWS accounts, so
  # this name must be changed before applying this example to avoid naming
  # conflicts.
  bucket = "test-bucket-mmda"
  acl    = "private"
}

resource "aws_key_pair" "example" {
  key_name   = "examplekey"
  public_key = file("~/.ssh/terraform.pub")
}

resource "aws_instance" "myFirst_Terraform_Instance" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
  tags = {
        Name = var.ec2-instance-name
       }
  depends_on = [aws_s3_bucket.my_first_bucket_mmda_colony]
  
 provisioner "local-exec" {
    command = "echo ${aws_instance.myFirst_Terraform_Instance.public_ip} > $HOME/ip_address.txt"
  }
  
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/terraform")
    host        = self.public_ip
  }

  provisioner "remote-exec" {
    inline = [
      "sudo amazon-linux-extras enable nginx1.12",
      "sudo yum -y install nginx",
      "sudo systemctl start nginx"
    ]
  }
  
} 

resource "aws_eip" "ip" {
    vpc = true
    instance = aws_instance.myFirst_Terraform_Instance.id
}


