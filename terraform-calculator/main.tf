provider "aws" {
  region = "eu-central-1"
}
resource "aws_security_group" "instance_sg" {
  name        = "instance_sg"
  description = "Allow SSH and HTTP access"
 
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
 
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
 
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
resource "aws_instance" "calculator" {
  ami           = "ami-017095afb82994ac7"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.instance_sg.name] 
  user_data = <<-EOF
              #!/bin/bash
              docker run -d -p 5000:5000 my-calculator
              EOF
  tags = {
    Name = "calculator-instance"
  }
}