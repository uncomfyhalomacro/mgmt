# 📅 Appointment & Queue Management System

A full-stack appointment scheduling and queue management system built with **FastAPI**, designed for small to medium service-based businesses (e.g. clinics, salons, consultation services).

This system allows customers to book appointments, staff to manage queues, and admins to oversee operations through a centralized dashboard.

## Initial setup

Requires [direnv](https://direnv.net/) and [nix](https://nixos.org).

```bash
mkdir -p ~/.config/direnv
# Either copy or append the layout script
cat $PROJECT_PATH/.direnv.uv >> ~/.config/direnv/direnvrc
direnv allow
```

---

## 🚀 Features

### 🔐 Authentication & Authorization
- Email/password authentication
- Role-based access control:
  - **Admin**
  - **Staff**
  - **Customer**
- Secure session handling (HTTP-only cookies or JWT)

---

### 📆 Appointment Booking
- View available time slots
- Book, cancel, or reschedule appointments
- Prevent double booking
- Enforce business hours and availability rules

---

### 👥 Queue Management (Staff)
- Check-in customers
- Update appointment status:
  - `scheduled`
  - `checked_in`
  - `in_progress`
  - `completed`
  - `no_show`
  - `cancelled`
- Real-time queue overview

---

### 🛠️ Service Management (Admin)
- Create and manage services
- Define:
  - duration
  - pricing
  - availability rules
- Assign services to staff

---

### 🗓️ Staff Scheduling
- Weekly recurring availability
- Blocked dates (holidays, leave)
- Schedule overrides

---

### 📊 Dashboard & Reporting
- Total bookings
- Revenue summary
- No-show rate
- Staff utilization
- Popular services

---

### 🔔 Notifications
- Appointment confirmation
- Reminder system (via background tasks)
- Cancellation alerts

---

### 📜 Audit Logging
- Track important actions:
  - appointment updates
  - schedule changes
  - admin operations

---

## 🧱 Tech Stack

### Backend
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy / SQLModel**
- **Alembic (migrations)**
- **Pydantic (validation)**
- **AnyIO (async runtime)**

### Frontend
- Any (React, Preact, Vue, etc.)

### Optional
- Redis (caching / background jobs)
- Email service (SendGrid, SMTP)

---

## 🏗️ Project Structure

```
backend
├── app
│   ├── api            # Route handlers
│   ├── core           # Config, Security, Utilities
│   ├── db             # DB Session dependencies
│   ├── models         # Database models
│   ├── schemas        # Schemas
│   ├── services       # Business logic layer
│   ├── __init__.py    # APIRouter
│   └── __main__.py    # Uvicorn entrypoint
├── migrations         # Alembic
└── tests/             # Unit & integration tests
```

---

## 📡 API Overview

### Auth
```
POST   /auth/register
POST   /auth/login
POST   /auth/logout
GET    /auth/me
```

### Services
```
GET    /services
POST   /services
PATCH  /services/{id}
DELETE /services/{id}
```

### Appointments
```
GET    /appointments
POST   /appointments
PATCH  /appointments/{id}
DELETE /appointments/{id}
```

### Queue (Staff)
```
PATCH  /appointments/{id}/status
GET    /queue
```

### Scheduling
```
GET    /staff/{id}/availability
POST   /staff/{id}/availability
```

---

## 🧠 Key Design Decisions

### Structured Business Logic
- Core logic separated into `services/`
- Routes remain thin and declarative

### Conflict Prevention
- Booking logic ensures:
  - no overlapping appointments
  - valid time slots only

### State Machine for Appointments
Each appointment follows a strict lifecycle:

```
scheduled → checked_in → in_progress → completed
                         ↘ no_show
scheduled → cancelled
```

---

## 🧪 Testing

```bash
pytest
```

Includes:
- booking conflict tests
- auth tests
- role permission tests

---

## 📈 Future Improvements

- Payment integration (Stripe)
- SMS/email reminders
- Google Calendar sync
- Multi-branch support
- Real-time updates (WebSockets)
- Public booking page

---

## 📌 Use Case

This system is designed for:
- Clinics
- Salons
- Consultation services
- Repair/service shops

---

## 🤝 Contributing

Contributions are welcome. Please open an issue or submit a PR.

---

## 📄 License

MIT License

