# Dependency injection: 
# Needs to be discussed

from fastapi import FastAPI, Depends, Header, HTTPException


from typing import Optional


app = FastAPI()


# ===== Simple Dependency =====


def get_db():


    """


    Dependency that returns a database connection.


    """


    # In real app, this would create/return a connection


    print("Creating database connection")


    return {"connection": "db_connection", "status": "connected"}


@app.get("/users")


async def get_users(db: dict = Depends(get_db)):


    """


    Endpoint that uses the database dependency.


    """


    return {


        "message": "Getting users",


        "db_status": db["status"],


        "users": ["Alice", "Bob", "Charlie"]


    }


# ===== Dependency with Parameters =====


def get_pagination(skip: int = 0, limit: int = 10):


    """


    Dependency for pagination.


    """


    return {"skip": skip, "limit": limit}


@app.get("/items")


async def get_items(pagination: dict = Depends(get_pagination)):


    """


    Endpoint with pagination dependency.


    """


    return {


        "pagination": pagination,


        "items": [f"Item {i}" for i in range(pagination['skip'], pagination['skip'] + pagination['limit'])]


    }


# ===== Dependency for Authentication =====


async def get_current_user(token: str = Header(...)):


    """


    Dependency that validates the user token.


    """


    if token != "secret-token":


        raise HTTPException(status_code=401, detail="Invalid token")


   


    return {"id": 1, "username": "alice", "role": "admin"}


@app.get("/profile")


async def get_profile(user: dict = Depends(get_current_user)):


    """


    Endpoint that requires authentication.


    """


    return {"user": user}


# ===== Nested Dependencies =====


async def get_optional_user(token: Optional[str] = Header(None)):


    """Dependency that gets user if token exists."""


    if token and token == "secret-token":


        return {"id": 1, "username": "alice"}


    return None


async def get_optional_db(connection: str = "default"):


    """Dependency that gets database connection."""


    return {"connection": connection}


@app.get("/public")


async def public_endpoint(


    db: dict = Depends(get_optional_db),


    user: Optional[dict] = Depends(get_optional_user)


):


    """


    Endpoint that works with or without authentication.


    """


    return {


        "message": "Public endpoint",


        "user": user,


        "db": db


    }


# ============================================================
# RUN APPLICATION
# ============================================================


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "P2:app",  # Replace test with your filename without .py
        host="127.0.0.1",
        port=8000,
        reload=True
    )


# open in your browser:
# http://127.0.0.1:8000/docs
# You’ll see all endpoints listed. Test them like this:

# 1. Test /users (simple dependency)
# Endpoint: GET /users

# Find GET /users.

# Click Try it out.

# Click Execute.

# Expected response:


# {
#   "message": "Getting users",
#   "db_status": "connected",
#   "users": [
#     "Alice",
#     "Bob",
#     "Charlie"
#   ]
# }
# This just uses the get_db dependency; no parameters needed.

# 2. Test /items (pagination dependency)
# Endpoint: GET /items

# Without parameters
# Find GET /items.

# Click Try it out.
# Leave skip and limit as default.
# Click Execute.

# Expected response:

# {
#   "pagination": {
#     "skip": 0,
#     "limit": 10
#   },
#   "items": [
#     "Item 0",
#     "Item 1",
#     "Item 2",
#     "Item 3",
#     "Item 4",
#     "Item 5",
#     "Item 6",
#     "Item 7",
#     "Item 8",
#     "Item 9"
#   ]
# }

# With custom pagination
# Set:
# skip: 2
# limit: 3

# Click Execute.

# Expected response:
# {
#   "pagination": {
#     "skip": 2,
#     "limit": 3
#   },
#   "items": [
#     "Item 2",
#     "Item 3",
#     "Item 4"
#   ]
# }
# 3. Test /profile (requires token header)
# Endpoint: GET /profile

# Your dependency expects a header:

# token: str = Header(...)
# Swagger will show a field named token under Parameters.

# With a valid token
# Find GET /profile.
# Click Try it out.

# In the token field, enter:

# secret-token
# Click Execute.

# Expected response:
# {
#   "user": {
#     "id": 1,
#     "username": "alice",
#     "role": "admin"
#   }
# }

# With an invalid token
# Change token to:

# wrong-token
# Click Execute.

# Expected response:
# {
#   "detail": "Invalid token"
# }
# Status code:

# 401 Unauthorized
# Without a token
# Clear the token field.
# Click Execute.

# Expected response:
# {
#   "detail": [
#     {
#       "type": "missing",
#       "loc": ["header", "token"],
#       "msg": "Field required"
#     }
#   ]
# }
# Status code:
# 422 Unprocessable Entity


# 4. Test /public (optional auth + optional DB)
# Endpoint: GET /public

# Dependencies:
# db: dict = Depends(get_optional_db)
# user: Optional[dict] = Depends(get_optional_user)

# get_optional_user expects:
# token: Optional[str] = Header(None)

# Swagger will show:
# connection (query parameter, default "default")
# token (header parameter, optional)

# Without any parameters
# Find GET /public.
# Click Try it out.

# Do not change anything.
# Click Execute.

# Expected response:
# {
#   "message": "Public endpoint",
#   "user": null,
#   "db": {
#     "connection": "default"
#   }
# }

# With a valid token
# In the token field, enter:
# secret-token
# Click Execute.

# Expected response:
# {
#   "message": "Public endpoint",
#   "user": {
#     "id": 1,
#     "username": "alice"
#   },
#   "db": {
#     "connection": "default"
#   }
# }

# With an invalid token
# In token, enter:
# wrong-token
# Click Execute.

# Expected response:
# {
#   "message": "Public endpoint",
#   "user": null,
#   "db": {
#     "connection": "default"
#   }
# }
# Because the token is optional, it just returns user: null instead of an error.

# With a custom DB connection name
# Set:
# connection: mydb
# token: secret-token
# Click Execute.

# Expected response:
# {
#   "message": "Public endpoint",
#   "user": {
#     "id": 1,
#     "username": "alice"
#   },
#   "db": {
#     "connection": "mydb"
#   }
# }