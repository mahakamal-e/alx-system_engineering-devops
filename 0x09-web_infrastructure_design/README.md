# Project Name
## 0x09. Web Infrastructure Design
### Overview
This project focuses on designing a robust web infrastructure to host the website www.foobar.com. The infrastructure includes multiple servers, load balancing, a web server (Nginx), application servers, and a MySQL database.

### Components:
#### 1. DNS Configuration:
Purpose: Resolve domain names to IP addresses and manage the routing of incoming requests.

#### 2. Web Server(Nginx):
Purpose: Serve as a front-end server for handling static content and forwarding dynamic requests to application servers.

#### 3. Application Servers:
Purpose: Execute server-side scripts, run business logic, and generate dynamic content.

#### 4. Database (MySQL):
Purpose: Store and manage data required by the web application.

#### 5. Load Balancer (HAproxy):
Purpose: Distribute incoming traffic among multiple servers for improved performance and fault tolerance.
Algorithm: Configured with a Round Robin distribution algorithm.
