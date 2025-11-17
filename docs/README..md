# User Stories

1 - As an **admin**, I want to **configure all user accounts and assign them the proper level access**, so I can **ensure seamless access to the system by proper privileges**.

**Acceptance Criteria**:
  -  Admin can create, and delete users.
  -  Role changes are effective immediatel

2 - As a **manager**, I want to **create a shipment in the system**, so I can **have it be tracked by the drivers and the customers**.

**Acceptance Criteria**:
  - Shipments are actually created
  - Shipments are assigned a tracking ID
  - Warehouse, sender, and recipient are identified

3 - As a manager, I want to **update shipment status to reflect on its proper location**, so I can **make sure that the customer understands where the shipment is**.

**Acceptance Criteria**:
  - Status updates automatically reflection
  - Updates include logs and timestamps

4 - As a manager, I want to **assign shipments to drivers**, so I can **have them deliver the shipments, and update their status**.

**Acceptance Criteria**:
  - Shipments are assigned in real time to drivers with their status

5 - As a delivery driver, I want** to see all shipments assigned to me and update their status**, so I can **update my manager and customers about their shipment**.

**Acceptance Criteria**:
  - Driver can only see their assigned shipments
  - Driver can update status of shipment to in progress, or delivered

6-  As a customer, I want to **be able to track the progress of my shipment**, so I can **know when to expect it to be delivered**. 

**Acceptance Criteria**:
  - Customer can log in
  - Customer can view package tracking ID.


# Misuse Stories

1 - As a **malicious driver**, I want to **falsify driving records and shipment status**, so I can **hide delays in delivering packages**.

**Mitigations**:
  - Log all actions by the user who performed them
  - Manager approval for all changes

2 - As an **unathorized user**, I want to **view other customers packages, and their details**, so I can **disccover shipments I am not supposed to see**.

**Mitigations**:
  - Hard to guess tracking IDs
  - Shipments are only assigned to their prespective customers

3 - **As a compromised manager account**, I want to **make role changes and mess around with access**, so I can **find interesting data**.

**Mitigations**:
  - Only admins can make role changes



# Diagrams
## Context Diagram
![Context Diagram](https://github.com/zkak345/Web_App/blob/main/docs/Context%20Diagram)

## Container Diagram
![Container Diagram](https://github.com/zkak345/Web_App/blob/main/docs/Container%20Diagram)

## Component Diagram
![Compontent Diagram](https://github.com/zkak345/Web_App/blob/main/docs/Component%20Diagram)


## UI interfaces
![UI](https://github.com/zkak345/Web_App/blob/main/docs/UI)
![UI2](https://github.com/zkak345/Web_App/blob/main/docs/UI2)
