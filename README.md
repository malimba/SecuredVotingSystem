# Secured Voting System

A **Django voting platform** built for school elections — nominee profiles, OTP gate, live vote counts, and AJAX-powered ballot submission.

![Django](https://img.shields.io/badge/Django-4.1-092E20?style=flat-square&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)

## Features

- **VoteNominee** model — photo, position, running vote tally
- OTP verification step before ballot access
- AJAX endpoints for casting votes
- SQLite backend for lightweight deployment
- Admin-friendly nominee management

## Tech stack

- **Django 4.1**
- **Pillow** — image uploads for nominee photos
- **SQLite**

## Quick start

```bash
cd SecuredVotingSystem
pip install django pillow
python manage.py migrate
python manage.py runserver
```

## Security note

Built for a **school election demo**. Review OTP handling, rate limiting, and voter authentication before any real-world use.

## Project layout

```
SecuredVotingSystem/
  manage.py
  votingapp/
    models.py    # VoteNominee
    views.py     # Ballot + OTP flows
    templates/
```

---

[malimba](https://github.com/malimba)
