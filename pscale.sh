# PlanetScale CLI
# Install
# MacOS
# brew install planetscale/tap/pscale
# brew install mysql-client
# brew upgrade pscale

# Linux
## Debian-based
# sudo apt-get install mysql-client
## RPM-based
# sudo yum install community-mysql

# Basic Usage
# pscale --help
# pscale login
# pscale version

#--------------------------------------
# PlanetScale Workflows
# 1. Create a database
# pscale database create <database>

# 2. Create a develop branch
# pscale branch create <database> <branch>

# 3. Make changes to the database
# pscale shell <database> <branch>

# 這裡就可以調整資料庫的內容
# Example code
CREATE TABLE `reminders` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `body` varchar(1024) NOT NULL,
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `is_done` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `queue` (
    `id` INT AUTO_INCREMENT PRIMARY KEY, 
    `name` VARCHAR(255), 
    `phone` VARCHAR(255), 
    `size` INT
    )

#修改增加 more column
ALTER TABLE queue ADD COLUMN `more` VARCHAR(255);

#新增
CREATE TABLE `queue2` (
    `id` INT AUTO_INCREMENT PRIMARY KEY, 
    `name` VARCHAR(255), 
    `phone` VARCHAR(255), 
    `size` INT
    )

# --Test your changes~ --

# 4. Create a deployment request
# pscale deploy-request create <database> <branch>

# 5. Review the deployment request~

# 6. Deploy the changes
# pscale deploy-request deploy <database> <deploy-request-number>


