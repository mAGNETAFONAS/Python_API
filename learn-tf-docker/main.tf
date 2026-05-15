terraform {
  required_version = ">= 1.0.0"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 4.2.0"
    }
  }
}

locals {
  version = trimspace(file("${path.module}/../VERSION.md"))
}

provider "docker" {}

resource "docker_image" "web" {
  name = "python-api-web:${local.version}"
}

resource "docker_network" "web_app" {
  name = "app_network"
}

resource "docker_volume" "db" {
  name = "db_data"
  driver = "local"
}

resource "docker_container" "web_app" {
  image = docker_image.web.image_id
  name  = "web_app"

  ports {
    internal = 8000
    external = 8000
  }
  env = [
    "MYSQL_ROOT_PASSWORD=${file("${path.module}/../root_pass.txt")}",
    "MYSQL_DATABASE=web",
    "MYSQL_USER=simas",
    "MYSQL_PASSWORD=${file("${path.module}/../user_pass.txt")}",
    "PEPPER=${file("${path.module}/../pepper.txt")}",
    "MYSQL_HOST=python-api-db"
  ]

  volumes {
    host_path = abspath("${path.module}/../files/")
    container_path = "/app/files"
  }

  networks_advanced {
    name = "app_network"
  }
}

resource "docker_container" "db" {
  image = "mysql:9.6.0"
  name  = "python-api-db"

  ports {
    internal = 3306
  }

  env = [
    "MYSQL_ROOT_PASSWORD=${file("${path.module}/../root_pass.txt")}",
    "MYSQL_DATABASE=web",
    "MYSQL_USER=simas",
    "MYSQL_PASSWORD=${file("${path.module}/../user_pass.txt")}",
  ]

  networks_advanced {
    name = "app_network"
  }

  volumes {
    volume_name = "db_data"
    container_path = "/var/lib/mysql"
  }

  volumes {
    host_path = abspath("${path.module}/../db_scripts/init.sql")
    container_path = "/docker-entrypoint-initdb.d/init.sql"
  }

  healthcheck {
    interval = "2s"
    retries = 1
    test = ["CMD", "mysqladmin", "ping", "-h", "localhost"]
  }
}
