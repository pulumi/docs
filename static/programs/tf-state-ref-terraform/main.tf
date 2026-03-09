terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

data "aws_region" "current" {}

locals {
  name = "convert-tf"
  azs = [
    "${data.aws_region.current.name}a",
    "${data.aws_region.current.name}b",
    "${data.aws_region.current.name}c",
  ]
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnet_cidrs = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
}

provider "aws" {}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = local.name
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "convert-tf"
  }
}

resource "aws_subnet" "public_subnets" {
  count             = length(local.public_subnet_cidrs)
  vpc_id            = aws_vpc.main.id
  availability_zone = element(local.azs, count.index)
  cidr_block        = element(local.public_subnet_cidrs, count.index)
  tags = {
    Name = "convert-tf-public-${count.index + 1}"
  }
}

resource "aws_route_table" "public_route_tables" {
  count  = length(local.public_subnet_cidrs)
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "convert-tf-public-${count.index + 1}"
  }
}

resource "aws_route_table_association" "public_route_table_associations" {
  count          = length(local.public_subnet_cidrs)
  subnet_id      = element(aws_subnet.public_subnets[*].id, count.index)
  route_table_id = aws_route_table.public_route_tables[0].id
}

resource "aws_route" "public_igw_route" {
  count                  = length(local.public_subnet_cidrs)
  route_table_id         = aws_route_table.public_route_tables[count.index].id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.igw.id

  timeouts {
    create = "5m"
  }
}

resource "aws_eip" "eip" {
  tags = {
    Name = local.name
  }
}

resource "aws_nat_gateway" "natgw" {
  subnet_id     = aws_subnet.public_subnets[0].id
  allocation_id = aws_eip.eip.allocation_id
  tags = {
    Name = local.name
  }
  depends_on = [aws_internet_gateway.igw]
}

resource "aws_subnet" "private_subnets" {
  count             = length(local.private_subnet_cidrs)
  vpc_id            = aws_vpc.main.id
  availability_zone = element(local.azs, count.index)
  cidr_block        = element(local.private_subnet_cidrs, count.index)
  tags = {
    Name = "convert-tf-private-${count.index + 1}"
  }

}

resource "aws_route_table" "private_route_tables" {
  count  = length(local.private_subnet_cidrs)
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "convert-tf-private"
  }
}

resource "aws_route_table_association" "private_route_table_associations" {
  count          = length(local.private_subnet_cidrs)
  subnet_id      = element(aws_subnet.private_subnets[*].id, count.index)
  route_table_id = aws_route_table.private_route_tables[count.index].id
}

resource "aws_route" "private_natgw_routes" {
  count                  = length(local.private_subnet_cidrs)
  route_table_id         = aws_route_table.private_route_tables[count.index].id
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id         = aws_nat_gateway.natgw.id

  timeouts {
    create = "5m"
  }
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "private_subnet_ids" {
  value = aws_subnet.private_subnets[*].id
}

output "public_subnet_ids" {
  value = aws_subnet.public_subnets[*].id
}
