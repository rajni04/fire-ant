# fire-ant
Timesheet on terminal

## Contribute

### Pre-requisites

- Python 3.11 +
- Postgresql

### Database Setup

1. Create database
1. Create user(non-superuser)
1. Grant access on database to user
1. Copy content from `config.toml.example` to a new file `config.toml`
1. Update `config.toml` with your database details
1. Check database connection `python main.py --check`

### 