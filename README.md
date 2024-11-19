# **Backend Setup for Login and Signup Services**

This repository contains the backend setup for managing login and signup services, complete with email verification functionality. The services are designed to leverage **Keycloak**, a robust open-source identity and access management solution, which is set up in a virtual machine (VM) in the cloud.

---

## **Keycloak Overview**

**Keycloak** is an open-source software solution that provides authentication and authorization services for applications. It simplifies user management by offering features like:

- **Single Sign-On (SSO):** Users can log in once and access multiple applications without the need to authenticate again.
- **Role-Based Access Control (RBAC):** Assign roles to users and manage access to resources.
- **User Federation:** Integrates with existing user directories like LDAP or Active Directory.
- **Social Login:** Supports login with third-party providers like Google, Facebook, and GitHub.
- **Extensibility:** Allows custom authentication flows, user storage, and integration with third-party tools.

### **How Keycloak Works**
1. **User Authentication:** Applications redirect users to Keycloak for authentication. Users can log in with credentials stored in Keycloak or via third-party identity providers.
2. **Token Issuance:** Upon successful authentication, Keycloak generates tokens (e.g., access tokens, refresh tokens) that applications use to validate user sessions.
3. **Session Management:** Keycloak manages user sessions and ensures secure logout across applications.
4. **Centralized Management:** Admins can manage users, roles, permissions, and application integrations from the Keycloak admin console.

This project uses Keycloak to handle user authentication and authorization for the backend services.

---

## **Project Features**

- **Login Service:** Secure user login functionality integrated with Keycloak for authentication.
- **Signup Service:** Allows users to register with email and password.
- **Email Verification:** Sends a unique verification code to the user's email during signup to ensure account validation.
- **Cloud Integration:** Keycloak is deployed in a cloud-based VM for scalability and reliability.

---

## **Why Few Commits?**

The limited number of commits in this repository is because the project was originally developed under a different repository. It was later migrated to this dedicated repository for better organization and management.

---

## **Setup and Deployment**

### **Prerequisites**
- **Keycloak:** Installed and running on a cloud VM.
- **Cloud SQL Proxy (Optional):** For secure database connections.
- **Docker (Optional):** For containerized deployment.

### **Steps to Run Locally**
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <project-folder>
